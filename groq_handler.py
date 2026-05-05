from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(message):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a customer support assistant for VELOUR clothing brand. Answer about pricing, sizing, delivery, and policies. Keep replies short and friendly."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        max_tokens=200
    )

    return response.choices[0].message.content