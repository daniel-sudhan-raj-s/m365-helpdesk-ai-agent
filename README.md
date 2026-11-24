# M365 Helpdesk AI Agent

An AI-powered IT helpdesk agent built with Python, Google ADK, and Gemini.

The project demonstrates how an AI agent can troubleshoot Microsoft 365 issues, call Python tools, create support tickets, and retrieve ticket status.

## Features

- Microsoft 365 troubleshooting assistance
- AI agent built using Google Agent Development Kit (ADK)
- Gemini-powered natural language interaction
- Tool calling based on user intent
- Ticket status lookup
- Support ticket creation and escalation
- Troubleshooting knowledge base for:
  - Outlook
  - Microsoft Teams
  - OneDrive
  - Password issues
  - VPN issues
- Secure API key management using environment variables

## Tools Implemented

### check_ticket_status
Retrieves the status of an IT support ticket using a ticket ID.

### get_troubleshooting_steps
Provides troubleshooting steps based on the application or issue reported by the user.

### create_ticket
Creates a simulated IT support ticket with Low, Medium, or High priority.

## Example Agent Flow

User:
My Teams is not working.

Agent:
Calls the troubleshooting tool and provides Teams troubleshooting steps.

User:
I tried the steps but the issue is still happening.

Agent:
Offers to create a support ticket.

User:
Yes, create a high priority ticket.

Agent:
Calls the ticket creation tool and returns a new incident number.

## Tech Stack

- Python
- Google Agent Development Kit (ADK)
- Gemini API
- Google Gen AI SDK
- python-dotenv
- Git
- GitHub

## Project Structure

```text
m365-helpdesk-ai-agent/
├── support_agent/
│   ├── __init__.py
│   └── agent.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
