from src import Voice2Voice


v2v_client = Voice2Voice(
    host="0.0.0.0",
    port=9090,
    lang="en",  # input language or transcription language
    translate=False,
    model="tiny",
    use_vad=False,
    save_output_recording=False,  # Only used for microphone input, False by Default
    output_recording_filename="./output_recording.wav",  # Only used for microphone input
    mute_audio_playback=False,  # Only used for file input, False by Default
    enable_translation=False,
    target_language="ur",
)


v2v_client()
