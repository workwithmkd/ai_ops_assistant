import pandas as pd
import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1️⃣ Load datasets
cases = pd.read_csv("data/cases.csv")
org_map = pd.read_csv("data/org_map.csv")

# 2️⃣ Pick a random open case
sample_case = cases[cases["status"] == "Open"].sample(1).iloc[0]

prompt = f"""
You are an AI triage assistant for a tech organization.
Each team handles specific issue areas:

{org_map.to_string(index=False)}

Given this new case:
Title: {sample_case['case_title']}
Description: {sample_case['case_description']}
Product Area: {sample_case['product_area']}
Priority: {sample_case['priority']}

Which team should handle it? Reply only with the team name and one-line reasoning.
"""

# 3️⃣ Ask GPT for triage decision
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

ai_reply = response.choices[0].message.content
print("🔍 AI Triager Decision:")
print(ai_reply)
