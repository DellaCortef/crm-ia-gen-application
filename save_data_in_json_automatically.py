import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configuration
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to create the wizard with File Search enabled
def create_assistant_with_file_search():
    assistant = client.beta.assistants.create(
        name= "My Sales Assistant",
        instructions="You are an assistant to help me with sales.",
        model="gpt-4o",
        tools=[{"type": "file_search"}]  # Enabling file_search
    )

    print(f"Wizard created with ID: {assistant}")
    return assistant

# Create a Vector Store to store files
def create_vector_store():
    vector_store = client.beta.vector_stores.create(
        name="Sales Data Store"
    )

    print(f"Vector Store created with ID: {vector_store.id}")
    return vector_store