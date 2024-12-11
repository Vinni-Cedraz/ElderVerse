# -*- coding: utf-8 -*-
# from groq import Groq import os
import os
import requests
from pathlib import Path
from collections import deque
from query_groq import query_groq
from ielder_bot import IElderBot
from story_bot import StoryBot


class ElderBot(IElderBot):
    def __init__(self, usecase):
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
        self.usecase = usecase

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


    def run(self):
        initial_message = (
            "Hello! I'm here to listen and make you company. What is your name?\n"
        )
        print(f"Elder Chatbot: {initial_message}")
        self.add_message("assistant", initial_message)

        while True:
            try:
                user_input = input()
            except EOFError:
                print("\nEOF detected. Exiting...")
                break

            if user_input.lower() == "quit":
                print("\nGenerating your story...")
                story_bot = StoryBot(self)
                story_bot.generate_story()
                print("\nYour story has been saved as a PDF!")
                break

            is_audio = False
            if (
                os.path.exists(user_input)
                and Path(user_input).suffix.lower() in self.audio_file_types
            ):
                is_audio = True

            response = self.get_bot_response(user_input, is_audio)
            print(f"Elder Chatbot: {response}")
