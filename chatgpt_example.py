import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send a question to GPT-4
def ask_chatgpt(question):
    """"
    Log function instantiating an openai client.
    Python function that asks ChatGPT and gets a response.
    """
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": ""}
        ]
    )

    # Extracting the actual content message from the response
    return response.choices[0].message.content

# Asking the question
question = "How much did I sell yesterday?"
answer = ask_chatgpt(question )

# Print the response
print(f"ChatGPT response: {answer}")