from piper import PiperVoice, SynthesisConfig
from src.tts.base import TTSBase
from src.common.utils import measure_time
from src.common.logger import log
from . import config


class PiperTTS(TTSBase):
    _instance = None
    _model = None

    # singleton pattern to load model only once
    def __new__(cls, *args, **kwargs):
        if cls._instance is None and cls._model is None:
            cls._instance = super(PiperTTS, cls).__new__(cls)
            cls.load_model()
        return cls._instance

    @classmethod
    def load_model(cls):
        with measure_time("Loaded TTS model", log):
            cls._model = PiperVoice.load(config.MODEL_PATH)

    def __init__(self):
        super().__init__()
        self.syn_config = SynthesisConfig(
            volume=config.VOLUME,
            length_scale=config.LENGTH_SCALE,  # twice as slow
            noise_scale=config.NOISE_SCALE,  # more audio variation
            noise_w_scale=config.NOISE_W_SCALE,  # more speaking variation
            normalize_audio=config.NORMALIZE_AUDIO,  # use raw audio from voice
        )

    def get_audio_streams(self, text):
        stream_chunks = []
        audio_generator = self._model.synthesize(text=text, syn_config=self.syn_config)
        for stream_chunk in audio_generator:
            # log.debug(stream_chunk.sample_rate)
            stream_chunks.extend(stream_chunk.audio_float_array.tolist())
        return stream_chunks
