import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
from tqdm import tqdm   # progress bar for iteration

# 1️⃣ Setup
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2️⃣ Load datasets
history = pd.read_csv("data/history.csv")
cases = pd.read_csv("data/cases.csv")
org_map = pd.read_csv("data/org_map.csv")

# Merge history with cases for context (case_id common)
data = history.merge(cases, on="case_id")

# 3️⃣ Function: Ask GPT to predict team for a case
def predict_team(case_title, case_description, product_area, priority):
    prompt = f"""
    You are an AI triage assistant for a tech organization.
    Each team handles specific issue areas:

    {org_map.to_string(index=False)}

    Given this new case:
    Title: {case_title}
    Description: {case_description}
    Product Area: {product_area}
    Priority: {priority}

    Which team should handle it? Reply with only the team name.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

# 4️⃣ Run predictions
predictions = []
for _, row in tqdm(data.iterrows(), total=len(data), desc="Evaluating cases"):
    predicted = predict_team(row["case_title"], row["case_description"], row["product_area"], row["priority"])
    predictions.append(predicted)

data["predicted_team"] = predictions

# 5️⃣ Evaluate accuracy
data["correct"] = data["predicted_team"].str.lower() == data["final_team"].str.lower()
accuracy = data["correct"].mean()

print("\n📊 Evaluation Results")
print(f"Total Cases Evaluated: {len(data)}")
print(f"Accuracy: {accuracy:.2%}")
print("\nSample of Predictions:")
print(data[["case_id", "predicted_team", "final_team", "correct"]].head())

# 6️⃣ Save results for analysis
data.to_csv("data/evaluation_results.csv", index=False)
print("\n✅ Evaluation results saved to ./data/evaluation_results.csv")
