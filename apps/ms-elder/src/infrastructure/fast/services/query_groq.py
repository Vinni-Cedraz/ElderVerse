from groq import Groq
import os


def query_groq(messages, model):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=list(messages),
        model=model,
    )
    return chat_completion.choices[0].message.content
