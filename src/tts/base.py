from abc import ABC, abstractmethod


class TTSBase(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_audio_streams(self, text: str) -> list:
        """Convert text to speech and return list of audio samples."""
        pass
