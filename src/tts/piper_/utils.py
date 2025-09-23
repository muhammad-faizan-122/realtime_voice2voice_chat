import sounddevice as sd
import threading


def play_audio(audio_np, sample_rate=22050):

    sd.play(audio_np, samplerate=sample_rate)
    sd.wait()


def play_audio_background(audio_np, sample_rate=22050):
    thread = threading.Thread(target=play_audio, args=(audio_np, sample_rate))
    thread.start()
    return thread  # Return thread to allow tracking
