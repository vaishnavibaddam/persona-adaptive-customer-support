import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY =", api_key)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(persona, query, context):

    prompt = f"""
You are an AI Customer Support Agent.

Customer Persona:
{persona}

Knowledge Base:
{context}

Customer Query:
{query}

Instructions:

Technical Expert:
- Detailed response
- Include troubleshooting steps
- Include root cause analysis

Frustrated User:
- Empathetic tone
- Simple language
- Reassuring

Business Executive:
- Concise
- Business-focused
- Minimal technical jargon

Only answer using the knowledge base provided.
If information is not available, recommend escalation.

Generate the response.
"""

    response = model.generate_content(prompt)

    return response.text