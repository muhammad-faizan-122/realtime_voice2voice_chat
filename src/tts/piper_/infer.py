from piper import PiperVoice, SynthesisConfig


voice = PiperVoice.load("src/tts/piper_/model/en_US-lessac-medium.onnx")
syn_config = SynthesisConfig(
    volume=1.0,  # half as loud
    length_scale=1.0,  # twice as slow
    noise_scale=1.0,  # more audio variation
    noise_w_scale=1.0,  # more speaking variation
    normalize_audio=False,  # use raw audio from voice
)


def get_tts_response_generator(text):
    stream_chunks = []
    for chunk_i, audio_chunk in enumerate(
        voice.synthesize(text, syn_config=syn_config)
    ):
        # print(audio_chunk.sample_rate, audio_chunk.audio_float_array)
        # print(audio_chunk)
        stream_chunks.extend(audio_chunk.audio_float_array.tolist())
        # print(len(audio_chunk.audio_float_array), type(audio_chunk.audio_float_array))
    return stream_chunks
