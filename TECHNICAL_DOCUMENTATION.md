TECHNICAL DOCUMENTATION
Qazaq-Space-AI

AI-Based Satellite Decision Support System
1. Project Description

Qazaq-Space-AI is an AI-based satellite telemetry analysis and decision-support system designed to simulate semi-autonomous satellite risk management.

The system processes telemetry parameters such as:

Energy level

Temperature

Signal strength

Based on these parameters, the AI module evaluates operational risk and generates actionable recommendations.

2. System Architecture

The system consists of the following components:

User Interface (Streamlit Dashboard)

Interactive control panel

Telemetry input sliders

Real-time visualization

AI Decision Engine

Risk evaluation logic

Threshold-based analysis

Recommendation generator

Visualization Module (Plotly)

Telemetry charts

Risk indicators

3. AI Decision Logic

The AI module evaluates risk levels using predefined thresholds:

NORMAL – Stable satellite condition

WARNING – Moderate risk detected

CRITICAL – Immediate action required

The system generates dynamic recommendations based on telemetry data.

Example:

Low energy → Recommend power-saving mode

High temperature → Recommend cooling protocol

Weak signal → Recommend antenna recalibration

This simulates intelligent autonomous satellite behavior.

4. Technologies Used

Python

Streamlit

Plotly

Rule-based AI Decision Logic

5. Installation Guide
pip install -r requirements.txt
streamlit run app.py
6. Usage Instructions

Open the dashboard.

Adjust telemetry parameters.

The AI module automatically evaluates risk.

The system displays the recommended action.

7. Project Structure
Qazaq-Space-AI/
│
├── app.py
├── requirements.txt
├── images/
│   └── satellite.PNG
└── README.md
8. Demonstration Video

Project demonstration video:
https://youtu.be/T8tyyE0w1bE

9. Development Team

Team Name: AI Uly Dala
