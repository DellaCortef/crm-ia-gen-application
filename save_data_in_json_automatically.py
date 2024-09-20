import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configuration
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))