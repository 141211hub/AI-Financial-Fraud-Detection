import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_summary(transaction, prediction, probability, risk):

    prompt = f"""
You are a Senior Banking Fraud Analyst.

Analyze the following financial transaction.

Transaction Details
-------------------
Amount: {transaction['Amount']}
Time: {transaction['Time']}

Prediction: {prediction}

Fraud Probability: {probability}%

Risk Level: {risk}

Transaction Features:
{transaction}

Write a professional fraud investigation report.

The report must contain:

1. Executive Summary

2. Risk Assessment

3. Possible Reasons

4. Recommended Banking Actions

5. Final Conclusion

Do NOT mention AI, machine learning, prediction models or algorithms.

Write like an experienced banking fraud investigator.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert banking fraud analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1000,
    )

    return response.choices[0].message.content