import os
import time
import streamlit as st
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API and Assistant ID configuration # asst_bWjV0p7J0MUiSt8nbl4TuMhG
ASSISTANT_ID = "asst_bWjV0p7J0MUiSt8nbl4TuMhG"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to send the question to the assistant and get the answer
def answer_the_question(question):
    # Create a new thread with the user's message
    
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"today is the day {datetime.now()} {question}",  # User question is sent directly
            }
        ]
    )

    # Send the thread to the wizard (as a new execution)
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    st.write(f"Conversation ID: {run.id}")

    # Wait for execution to complete
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        st.write(f"🏃 Run Status: {run.status}")
        time.sleep(1)

    st.write(f"🏁 Run Completed!")

    # Get the last message in the thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    # Extract and return the most recent response
    latest_message = messages[0]
    return latest_message.content[0].text.value.strip()

# Streamlit Interface
st.title("Customer Service Agent - Ask the Assistant")

# Inbox for questions
question = st.text_input("Input your question:")

# When a question is asked, send it to the assistant and display the answer
if question:
    answer = answer_the_question(question)
    st.write(f"💬 Answer: {answer}")