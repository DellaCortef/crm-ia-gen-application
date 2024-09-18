import os
from groq import Groq
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to send a question to GPT-4
def ask_chatgpt(question: str):
    """"
    Log function instantiating an groc client.
    Python function that asks GROC and gets a response.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)

question = "How much did I sell yesterday?"
answer   = ask_chatgpt(question)

pprint(answer)