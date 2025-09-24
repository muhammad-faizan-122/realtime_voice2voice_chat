import pyaudio
import wave

# -- Parameters from your working arecord command --
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 4096
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "pyaudio_test.wav"  # The name of the file to save

# --- Main Recording Logic ---
p = None
stream = None
frames = []  # A list to hold all the audio chunks

try:
    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print(f"* Recording for {RECORD_SECONDS} seconds...")

    # This loop reads audio in chunks for the specified duration
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        audio_chunk = stream.read(CHUNK)
        frames.append(audio_chunk)  # Add the chunk to our list

    print("* Done recording.")

except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    print("Stopping stream and cleaning up.")
    if stream:
        stream.stop_stream()
        stream.close()
    if p:
        p.terminate()

# --- Saving the audio to a .wav file ---
if frames:
    print(f"Saving audio to {WAVE_OUTPUT_FILENAME}...")
    wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))  # Join all the chunks and write them
    wf.close()
    print("Save complete.")
