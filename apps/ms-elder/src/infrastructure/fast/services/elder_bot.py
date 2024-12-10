#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from groq import Groq import os
import os
import requests
from pathlib import Path
from datetime import datetime
from collections import deque
from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from groq import Groq


def query_groq(messages, model):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=list(messages),
        model=model,
    )
    return chat_completion.choices[0].message.content

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

    @abstractmethod
    def generate_story(self):
        pass

    @abstractmethod
    def save_as_pdf(self, blog_content: str) -> str:
        pass


class ElderBotService(IElderBot):
    def __init__(self):
        self.max_messages = 15
        self.messages = deque(maxlen=self.max_messages)
        self.messages.append(
            {
                "role": "system",
                "content": """You are a friendly and patient chatbot speaking with an elderly person.
                Show genuine interest in their stories and experiences.""",
            }
        )
        self.user_name = None
        self.user_image = None

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        self.audio_file_types = (
            ".flac",
            ".mp3",
            ".mp4",
            ".mpeg",
            ".mpga",
            ".m4a",
            ".ogg",
            ".wav",
            ".webm",
        )

    def transcribe_audio(self, audio_file_path):
        """Transcribe audio file using Groq API"""
        if not Path(audio_file_path).suffix.lower() in self.audio_file_types:
            raise ValueError(
                f"Unsupported audio format. Supported formats: {self.audio_file_types}"
            )

        url = "https://api.groq.com/openai/v1/audio/transcriptions"
        headers = {"Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}"}

        with open(audio_file_path, "rb") as f:
            files = {"file": f}
            data = {"model": "whisper-large-v3"}
            response = requests.post(url, headers=headers, files=files, data=data)

        if response.status_code == 200:
            return response.json()["text"]
        else:
            raise Exception(f"Transcription failed: {response.text}")

    def get_bot_response(self, user_input, is_audio_file=False):
        if is_audio_file:
            try:
                transcribed_text = self.transcribe_audio(user_input)
                return self.get_bot_response(transcribed_text)
            except Exception as e:
                return f"Sorry, I couldn't process the audio: {str(e)}"

        # Existing text-based response code
        self.add_message("user", user_input)
        response = query_groq(self.messages, model="llama-3.2-11b-vision-preview")
        self.add_message("assistant", response)
        return response

    def generate_story(self):
        story_prompt = {
            "role": "system",
            "content": """Create a blog post from the following conversation. 
            The blog post should:
            1. Have an engaging title
            2. Be structured in clear sections
            3. Focus on the most interesting life stories and insights shared
            4. Include direct quotes when relevant
            5. Have a thoughtful conclusion
            6. Be between 500-1000 words
            7. Don't use markdown, because the final format will be a pdf.
            Format the response with the title on top, followed by the content in paragraphs.""",
        }

        # Create a temporary message list for story generation
        story_messages = [
            story_prompt,
            {"role": "user", "content": str(list(self.messages))},
        ]

        blog_post = query_groq(story_messages, model="llama-3.1-70b-versatile")
        self.save_as_pdf(blog_post)
        return blog_post

    def save_as_pdf(self, blog_content):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"elder_story_{timestamp}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "CustomTitle", parent=styles["Heading1"], fontSize=24, spaceAfter=30
        )

        content_parts = blog_content.split("\n", 1)
        title = content_parts[0]
        body = content_parts[1] if len(content_parts) > 1 else ""

        story = []
        story.append(Paragraph(title, title_style))

        if self.user_image and os.path.exists(self.user_image):
            img = Image(self.user_image, width=300, height=300)
            story.append(img)
        story.append(Spacer(1, 20))

        for paragraph in body.split("\n\n"):
            if paragraph.strip():
                story.append(Paragraph(paragraph, styles["Normal"]))
                story.append(Spacer(1, 12))

        doc.build(story)
        return filename

"""
@TODO: refactor this main into discrete functions - that throw 
"""
def main():
    chatbot = ElderBotService()
    initial_message = "Hello! I'd love to chat with you. You can type your message or provide the path to an audio file."
    print(f"Elder Chatbot: {initial_message}")
    chatbot.add_message("assistant", initial_message)

    while True:
        try:
            user_input = input(
                "Hi, I'm here to listen and make you company. What is your name?"
            )
        except EOFError:
            print("\nEOF detected. Exiting...")
            break

        if user_input.lower() == "quit":
            print("\nGenerating your story...")
            chatbot.generate_story()
            print("\nYour story has been saved as a PDF!")
            break

        is_audio = False
        if (
            os.path.exists(user_input)
            and Path(user_input).suffix.lower() in chatbot.audio_file_types
        ):
            is_audio = True

        response = chatbot.get_bot_response(user_input, is_audio)
        print(f"Elder Chatbot: {response}")


if __name__ == "__main__":
    main()
