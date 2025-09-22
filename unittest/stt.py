from src.stt.WhisperLive.whisper_live.client import VoiceAgent


client = VoiceAgent(
    "0.0.0.0",
    9090,
    lang="en",  # input language or transcription language
    translate=False,
    model="medium",
    use_vad=False,
    save_output_recording=True,  # Only used for microphone input, False by Default
    output_recording_filename="./output_recording.wav",  # Only used for microphone input
    mute_audio_playback=False,  # Only used for file input, False by Default
    enable_translation=False,
    target_language="ur",
)


client()
