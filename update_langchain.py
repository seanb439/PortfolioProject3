#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Project

# Update LangChain Agent Project (id=4)
project = Project.objects.get(id=4)

project.summary = "Built a command-line AI chat assistant built using Python, LangChain, and Google Gemini AI. The application allows users to interact with an AI-powered assistant through a continuous chat interface. The assistant is designed to provide clear, concise, and professional responses while maintaining conversation history throughout the session."

project.description = """The project began by setting up the development environment and installing the required dependencies. Environment variables were configured using a .env file to securely store the Gemini API key instead of hardcoding sensitive credentials directly into the program.

Next, the Google Gemini model was initialized using the ChatGoogleGenerativeAI class. The model was configured with a temperature value of 0 to ensure responses remained focused and deterministic.

An AI agent was then created using LangChain's create_agent() function. A system prompt was included to define the assistant's behavior, ensuring that responses remained professional, polite, and safe.

The main functionality of the application was built using a continuous while loop that:
1. Accepts user input
2. Sends the conversation history to the AI model
3. Receives and displays the assistant's response
4. Updates the chat history for contextual memory

Error handling was added using a try-except block to prevent crashes if unexpected response formatting occurred."""

project.tools_used = """• Python – Core programming language
• LangChain – Framework for creating AI agents and workflows
• Google Gemini API – Large Language Model used for generating responses
• dotenv – Used for securely loading API keys from environment variables"""

project.key_features = """• Interactive command-line chat interface
• Persistent conversation history during runtime
• Secure API key management
• AI-generated responses using Gemini 2.5 Flash
• Graceful program termination with bye or exit
• Basic exception handling for improved reliability"""

# Clear the fields that should be removed
project.role_contribution = ""
project.business_problem = ""

project.save()

print("✓ LangChain project updated successfully!")
print(f"Summary: {project.summary[:80]}...")
print(f"Tools: {project.tools_used[:80]}...")
print(f"Features: {project.key_features[:80]}...")
