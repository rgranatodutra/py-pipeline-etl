import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "You are a banking marketing expert."
                },
            {
                "role": "user", 
                "content": f"Create a custom message about importance of investments for fantasy user: \"{user['name']}\". (Max 100 characters)"
            }
        ]
    )

    return completion.choices[0].message.content
    