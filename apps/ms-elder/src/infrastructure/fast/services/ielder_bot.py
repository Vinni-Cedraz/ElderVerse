from abc import ABC, abstractmethod


class IElderBot(ABC):
    @abstractmethod
    def add_message(self, role: str, content: str):
        pass

    @abstractmethod
    def transcribe_audio(self, audio_file_path: str) -> str:
        pass

    @abstractmethod
    def get_bot_response(self, user_input: str, is_audio_file: bool = False) -> str:
        pass
