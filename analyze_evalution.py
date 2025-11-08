import pandas as pd

# 1️⃣ Load evaluation results
df = pd.read_csv("data/evaluation_results.csv")

# 2️⃣ Basic Overview
total_cases = len(df)
accuracy = df["correct"].mean()

print("📊 Evaluation Summary")
print(f"Total Cases Evaluated: {total_cases}")
print(f"Overall Accuracy: {accuracy:.2%}")
print("-" * 40)

# 3️⃣ Team-wise Accuracy
team_accuracy = (
    df.groupby("final_team")["correct"]
    .mean()
    .sort_values(ascending=False)
)

print("\n🏆 Accuracy by Team:")
print(team_accuracy)

# 4️⃣ Common Misroutes (AI → Actual)
misroutes = (
    df[df["correct"] == False]
    .groupby(["predicted_team", "final_team"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)

print("\n⚠️ Common Misroutes:")
print(misroutes.head(10))

# 5️⃣ Sample Correct / Incorrect Cases
print("\n✅ Example Correct Predictions:")
print(df[df["correct"] == True][["case_id", "case_title", "predicted_team", "final_team"]].head(3))

print("\n❌ Example Incorrect Predictions:")
print(df[df["correct"] == False][["case_id", "case_title", "predicted_team", "final_team"]].head(3))
