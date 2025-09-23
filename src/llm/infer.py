from llama_cpp import Llama
from src.common.logger import log
from src.common.utils import measure_time
from src.llm import config


class LLM:
    def __init__(self):
        pass

    def get_llm_stream_out():
        return


class LlamaGGUF(LLM):
    _instance = None
    llm = None

    # singleton pattern for load the LLM model only once
    def __new__(cls, *args, **kwargs):
        if not cls._instance and not cls.llm:
            cls._instance = super(LlamaGGUF, cls).__new__(cls)
            cls.llm = cls.load_llm()
        return cls._instance

    @classmethod
    def load_llm(cls):
        with measure_time("LLM model instance loading time", log):
            llm = Llama(
                model_path=config.MODEL_PATH,
                n_gpu_layers=config.GPU_LAYER,
                seed=config.SEED,
                n_ctx=config.CTX_LEN,
                verbose=config.VERBOSE,
            )
        return llm

    def __init__(self):
        self.messages = [
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": ""},
        ]

    def get_llm_generator(self, query):
        self.messages[1]["content"] = query
        log.debug(f"LLM Prompt: {self.messages}")
        try:
            with measure_time("instantiate generator time: ", log):
                generator = self.llm.create_chat_completion(
                    max_tokens=config.MAX_TOKENS,
                    temperature=config.TEMPERATURE,
                    stream=config.ALLOW_STREAM,
                    messages=self.messages,
                )
                return generator

        except Exception as e:
            log.error(f"LLM model inference error: {e}")
            return None

    def get_llm_stream_out(self, chunk):
        try:
            llm_response = chunk["choices"][0]["delta"]["content"]
            return llm_response
        except Exception as e:
            return None
