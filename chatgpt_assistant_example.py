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