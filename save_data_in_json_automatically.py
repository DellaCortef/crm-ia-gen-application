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

# Upload JSON files to Vector Store and wait for processing
def upload_files_to_vector_store(vector_store, file_paths):
    file_streams = []
    for file_path in file_paths:
        try:
            with open(file_path, "rb") as file:
                file_streams.append(file)
            print(f"File {file_path} prepared for upload.")
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    if file_streams:
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id, files=file_streams
        )

        print(f"Upload status: {file_batch.status}")
        print(f"File count: {file_batch.file_counts}")
    else:
        print("No files have been prepared for upload.")

# Update the wizard to use Vector Store
def update_assistant_with_vector_store(assistant, vector_store):
    client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {vector_store_ids: [vector_store_id]}},
    )

    print("Updated wizard for using Vector Store.")

