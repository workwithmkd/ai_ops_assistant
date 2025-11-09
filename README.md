# 🤖 AI-Ops Triage Assistant

An AI-powered system that automatically routes support and operational cases to the correct owning team using GPT reasoning and organizational skill maps.

This project simulates how AI can streamline enterprise triage workflows — reducing manual errors, improving response time, and enabling intelligent ownership routing across teams like **FinOps**, **Infra**, **Support**, and **Security**.


## 🧭 Overview

Traditional operations teams rely on manual triagers or rule-based routing, which often causes misroutes and ownership confusion when multiple teams are involved.

The **AI-Ops Triage Assistant** uses natural language understanding and historical data to:
- Read a case’s description and context
- Infer which team should handle it
- Evaluate accuracy against real historical triage data
- Provide insights on misroutes and opportunities for automation

This is the **v1.0** release — a working prototype demonstrating the foundation of AI-driven operational intelligence.

## 🧠 Architecture

📂 ai_ops_assistant/
├── data/
│ ├── cases.csv
│ ├── history.csv
│ ├── org_map.csv
│ ├── evaluation_results.csv
│
├── evaluate_triage.py # GPT-based triage prediction & evaluation
├── analyze_evaluation.py # Accuracy and misroute analysis
├── visualize_evaluation.py # Chart and heatmap visualization
├── evaluation_dashboard.ipynb # Combined interactive dashboard
├── requirements.txt # Dependencies
├── .env # API key (not committed)
└── README.md


---




