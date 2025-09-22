from llama_cpp import Llama
from src.common.logger import log
import time


class LLM:
    def __init__(self):
        pass

    def execute():
        return


s = time.time()
llm = Llama(
    model_path="src/llm/model/Llama-3.2-1B-Instruct-IQ3_M.gguf",
    n_gpu_layers=-1,  # Uncomment to use GPU acceleration
    seed=1337,  # Uncomment to set a specific seed
    n_ctx=2048,  # Uncomment to increase the context window
    verbose=False,
)
log.info(f"LLM model instance loading time {time.time()-s}")


def get_llm_response_generator(query):
    s = time.time()
    messages = [
        {
            "role": "system",
            "content": "You are a helpful bot assitant.  Your response must be concise, friendly and professional",
        },
        {"role": "user", "content": query},
    ]
    log.debug(f"LLM input messages: {messages}")
    output = llm.create_chat_completion(
        max_tokens=100,
        temperature=0.0,
        stream=True,
        messages=messages,
    )

    log.info("instantiate generator time: ", time.time() - s)
    return output
