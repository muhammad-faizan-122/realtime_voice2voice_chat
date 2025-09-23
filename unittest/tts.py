import sys
import os

sys.path.append(os.getcwd())

from common.text_to_speech import TextToSpeechStreamer
from src.llm.infer import LlamaGGUF


if __name__ == "__main__":
    query = input("enter your query: ")
    while not query.strip():
        print("Please enter a valid query.")
        query = input("enter your query: ")

    llm = LlamaGGUF()
    tts = TextToSpeechStreamer(llm)
    tts.stream_and_play(query)
