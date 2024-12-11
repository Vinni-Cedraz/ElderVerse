from abc import ABC, abstractmethod


class IStoryBot(ABC):
    @abstractmethod
    def generate_story(self):
        pass

    @abstractmethod
    def save_as_pdf(self, blog_content: str) -> str:
        pass
