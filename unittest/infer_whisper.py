from faster_whisper import WhisperModel

model_pth = ""

if not model_pth:
    raise ValueError("Please whisper model path...")

audio_pth = "src/stt/WhisperLive/pyaudio_test.wav"


if not audio_pth:
    raise ValueError("Please Audio file path...")

model = WhisperModel(model_pth, device="cpu")
segments, info = model.transcribe(audio_pth, beam_size=5, language="en")

print(
    "Detected language '%s' with probability %f"
    % (info.language, info.language_probability)
)
output = [segment for segment in segments]

for out in output:
    prob = getattr(out, "no_speech_prob", 0)
    print(prob)
