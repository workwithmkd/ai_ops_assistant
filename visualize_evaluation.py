import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load Data
df = pd.read_csv("data/evaluation_results.csv")

# 2️⃣ Compute Team-wise Accuracy
team_accuracy = (
    df.groupby("final_team")["correct"]
    .mean()
    .sort_values(ascending=False)
)

# 3️⃣ Plot Accuracy by Team
plt.figure(figsize=(8, 4))
sns.barplot(x=team_accuracy.index, y=team_accuracy.values, palette="viridis")
plt.title("Team-wise AI Triage Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Team")
plt.ylim(0, 1)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# 4️⃣ Misroute Heatmap
pivot = (
    df.groupby(["final_team", "predicted_team"])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(6, 5))
sns.heatmap(pivot, annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)
plt.title("Misroute Matrix: Actual vs Predicted Teams")
plt.xlabel("Predicted Team")
plt.ylabel("Actual Team")
plt.tight_layout()
plt.show()
