#!/usr/bin/env python3
import os
import dspy
from dspy import context
import json
from uuid import uuid4
from datetime import datetime
import glob

key = os.getenv("GROQ_API_KEY")
llm = dspy.GROQ(model="llama-3.2-11b-vision-preview", api_key=key)


# Define the chatbot function
def chatbot(prompt, conversation_history):
    with context():
        conversation_history.append({"role": "user", "content": prompt})
        context_texts = " ".join(
            [f"{turn['role']}: {turn['content']}" for turn in conversation_history]
        )
        response = llm(f"{context_texts}\nBot:")
        if isinstance(response, list):
            response = " ".join(response)
        response = response.strip('[]"')
        response_parts = response.split("\n")
        for part in response_parts:
            conversation_history.append({"role": "bot", "content": part})
        return response


# Function to get or create the user's UUID
def get_user_uuid(username):
    user_uuids = {}
    if os.path.exists("user_uuids.json"):
        with open("user_uuids.json", "r") as file:
            user_uuids = json.load(file)
    if username in user_uuids:
        user_uuid = user_uuids[username]
        print(f"Welcome back, {username}!")
    if username not in user_uuids:
        user_uuid = str(uuid4())
        user_uuids[username] = user_uuid
        with open("user_uuids.json", "w") as file:
            json.dump(user_uuids, file)
        print(f"Hello, {username}! Your new UUID is {user_uuid}")
    return user_uuid


def load_conversation_history(user_uuid):
    history_files = glob.glob(f"history/{user_uuid}_*_history.json")
    if history_files:
        # Get the most recently created file
        history_file = max(history_files, key=os.path.getctime)
        with open(history_file, "r") as file:
            return json.load(file)
    return []


# Save conversation history to file
def save_conversation_history(conversation_history, user_uuid, timestamp):
    history_file = f"history/{user_uuid}_{timestamp}_history.json"
    with open(history_file, "w") as file:
        json.dump(conversation_history, file)


# Main function to hold a conversation with the user
def main():
    username = input("Please enter your username: ")
    user_uuid = get_user_uuid(username)
    conversation_history = load_conversation_history(user_uuid)
    print("Chatbot: Hello! How can I assist you today?")
    timestamp = datetime.now()

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Goodbye!")
                save_conversation_history(conversation_history, user_uuid, timestamp)
                break
            response = chatbot(user_input, conversation_history)
            print(f"Chatbot: {response}")
    except EOFError:
        print("\nChatbot: Goodbye!")
        save_conversation_history(conversation_history, user_uuid, timestamp)


if __name__ == "__main__":
    main()
