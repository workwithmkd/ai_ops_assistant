import pandas as pd
import random

# ----- 1. CASE LEVEL DATA -----
case_titles = [
    "Payment API Timeout", "Refund Delay", "Login Failure",
    "Deployment Rollback", "Security Token Error", "Account Setup Issue"
]
product_areas = ["Payments", "Billing", "Infra", "Security", "Support"]
priorities = ["Low", "Medium", "High"]
sources = ["Customer Ticket", "Internal Alert", "Slack Escalation"]

cases = []
for i in range(1, 51):  # 50 sample cases
    title = random.choice(case_titles)
    cases.append({
        "case_id": f"C{i:03}",
        "case_title": title,
        "case_description": f"Auto-generated example describing {title.lower()}",
        "priority": random.choice(priorities),
        "source": random.choice(sources),
        "product_area": random.choice(product_areas),
        "current_owner": random.choice(["Support", "Infra", "FinOps", "Security"]),
        "status": random.choice(["Open", "In-Progress", "Closed"])
    })

pd.DataFrame(cases).to_csv("data/cases.csv", index=False)

# ----- 2. ORG SKILLSET MAP -----
org_map = [
    ["FinOps", "Payments,Billing", "Refunds", "People assume FinOps owns refunds"],
    ["Infra", "Deployment,Downtime", "API logic", "Infra handles downtime, not logic errors"],
    ["Support", "Customer queries,Account setup", "Code issues", "Support handles only Tier 1"],
    ["Security", "Access,Encryption", "UI bugs", "Security doesn’t manage UI problems"],
]
pd.DataFrame(org_map, columns=["team_name","primary_areas","excluded_areas","known_misconceptions"])\
  .to_csv("data/org_map.csv", index=False)

# ----- 3. HISTORICAL DATA -----
history = []
for i in range(1, 51):
    history.append({
        "case_id": f"C{i:03}",
        "case_type": random.choice(case_titles),
        "routed_team": random.choice(["Support", "Infra", "FinOps", "Security"]),
        "final_team": random.choice(["Support", "Infra", "FinOps", "Security"]),
        "resolution_summary": "Sample past resolution outcome",
        "resolution_time_hours": random.randint(2, 24),
        "repeat_routing": random.choice([0, 1])
    })

pd.DataFrame(history).to_csv("data/history.csv", index=False)

print("✅ Mock datasets created successfully in ./data/")
