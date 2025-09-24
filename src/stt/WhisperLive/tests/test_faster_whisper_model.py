from faster_whisper import WhisperModel


model = WhisperModel("faster_whisper_tiny", device="cpu", compute_type="int8")

segments, info = model.transcribe("audio.mp3")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
