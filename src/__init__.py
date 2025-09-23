from src.common.text_to_speech import TextToSpeechStreamer
from src.llm.infer import LlamaGGUF


if __name__ == "__main__":

    # logic for voice to text
    user_voice_text = input("enter your query: ")

    while not user_voice_text.strip():
        print("Please enter a valid query.")
        user_voice_text = input("enter your query: ")

    llm = LlamaGGUF()
    tts = TextToSpeechStreamer(llm)
    tts.stream_and_play()
