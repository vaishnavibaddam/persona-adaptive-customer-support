# Persona Adaptive Customer Support Agent

## Overview

This project is an AI-powered customer support system that adapts responses based on the customer's persona. It retrieves relevant information from a knowledge base, provides personalized responses, escalates sensitive issues, and generates a human handoff summary when required.

## Features

* Persona Detection
* Knowledge Base Retrieval
* Adaptive Responses
* Escalation Logic
* Human Handoff Summary
* Streamlit User Interface

## Supported Personas

### Technical Expert

Receives detailed technical explanations and troubleshooting guidance.

### Frustrated User

Receives empathetic and easy-to-understand responses.

### Business Executive

Receives concise, business-focused summaries.

## Project Structure

app.py

persona.py

rag.py

escalation.py

handoff.py

requirements.txt

README.md

docs/

## Knowledge Base Documents

* login.txt
* password_reset.txt
* account_lock.txt
* billing.txt
* refund.txt
* api_errors.txt
* subscription.txt
* security.txt
* performance.txt
* troubleshooting.txt

## Architecture

User Query

↓

Persona Detection

↓

Knowledge Base Retrieval

↓

Response Generation

↓

Escalation Check

↓

Human Handoff Summary

## Installation

pip install -r requirements.txt

## Run

streamlit run app.py

## Sample Queries

* API authentication is failing with error 401
* I have tried everything and nothing works
* How does this issue impact operations?
* I want a refund for my subscription
* My account is locked after multiple login attempts
