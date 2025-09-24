from piper import SynthesisConfig


MODEL_PATH = "src/tts/piper_/model/en_US-lessac-medium.onnx"
VOLUME = 1.0  # half as loud
LENGTH_SCALE = 1.0  # twice as slow
NOISE_SCALE = 1.0  # more audio variation
NOISE_W_SCALE = 1.0  # more speaking variation
NORMALIZE_AUDIO = False  # use raw audio from voice
