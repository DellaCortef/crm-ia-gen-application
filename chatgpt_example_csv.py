import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure your API key as an environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to read CSV file using pandas
def read_sales_data(file_path):
    try:
        # Read the csv file
        sales_data = pd.read_csv(file_path)
        print("Sales data uploaded successfully:")
        
        # Show the first lines of dataset
        print(sales_data.head())

        return sales_data
    
    except FileNotFoundError:
        print("File not found. Check the file path.")

        return None
    

# Function to send a question to Groq with data in JSON
def ask_groq(question, data_json):
    # Create the message content with the question and data in JSON
    content = {
        "question": question,
        "sales_data": data_json
    }

    # Send the question and data to Groq
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": str(content)}],
        model="llama3-8b-8192"  # Certifique-se de escolher o modelo correto
    )
    
    # Extracting the content of the response
    return chat_completion.choices[0].message.content

# Path to the sales.csv file
file_path = "sales.csv"

# Read data from CSV
sales_data = read_sales_data(file_path)

# Check if the data was loaded successfully
if sales_data is not None:
    # Convert DataFrame to JSON
    sales_data_json = sales_data.to_json(orient="records")

    # Asking the question to Groq with the data in JSON
    question = "How much did we sell on September 2nd?"
    answer = ask_groq(question, sales_data_json)

    # Print the response
    print(f"Groq answer: {answer}")

else:
    print("The question could not be sent to Groq due to an error reading the data.")