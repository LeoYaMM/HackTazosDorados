
from groq import Groq

client = Groq(
    api_key="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",
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)