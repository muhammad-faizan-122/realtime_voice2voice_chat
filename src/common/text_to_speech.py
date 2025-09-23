from src.common.logger import log
from src.tts.piper_.infer import get_tts_response_generator
from src.tts.piper_.utils import play_audio_background
from src.llm.infer import LlamaGGUF
import numpy as np


class TextToSpeechStreamer:
    def __init__(self, llm: LlamaGGUF):
        self.llm = llm
        self.audio_thread = None
        self.text_stream = []

    def is_sentence_end(self, token: str) -> bool:
        return token.strip().endswith((".", "!", "?"))

    def wait_for_previous_audio(self):
        if self.audio_thread and self.audio_thread.is_alive():
            self.audio_thread.join()

    def play_audio(self, text_chunk: str, final: bool = False):
        audio_stream = get_tts_response_generator(text_chunk)
        self.wait_for_previous_audio()

        log.debug(f"{'Final' if final else 'Intermediate'} TTS: {text_chunk}")
        self.audio_thread = play_audio_background(np.array(audio_stream))

        if final:
            self.audio_thread.join()

    def stream_and_play(self, user_query: str):
        try:
            generator = self.llm.get_llm_generator(user_query)
            if not generator:
                raise RuntimeError("LLM generator not initialized.")

            for chunk in generator:
                token = self.llm.get_llm_stream_out(chunk)
                if not token:
                    continue

                self.text_stream.append(token)

                if not self.is_sentence_end(token):
                    continue

                text_chunk = " ".join(self.text_stream)
                self.play_audio(text_chunk)
                self.text_stream.clear()

            # Play remaining text (if any)
            if self.text_stream:
                text_chunk = " ".join(self.text_stream)
                self.play_audio(text_chunk, final=True)
            else:
                self.wait_for_previous_audio()

            return "done"

        except Exception as e:
            log.error(f"Error in text-to-speech streaming: {e}")
            return "error"
