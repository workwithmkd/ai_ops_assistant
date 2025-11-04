# test_api.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load your .env file
load_dotenv()

# 2. Create a client using your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 3. Define your prompt
prompt = "Summarize this: The operations team processed 500 tickets today with 95% SLA compliance."

# 4. Send the prompt to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

# 5. Print the model's reply
print(response.choices[0].message.content)
