from google.adk.agents import Agent

# ---------- Sample data (stands in for a real ticketing system) ----------
TICKETS = {
    "INC1001": "Resolved - Outlook password reset completed",
    "INC1002": "In Progress - Teams login issue assigned to L2",
    "INC1003": "Pending - Waiting for user confirmation",
}

KNOWLEDGE_BASE = {
    "outlook": [
        "Close Outlook completely and reopen it.",
        "Check your internet connection and sign in again.",
        "Clear saved passwords in Windows Credential Manager.",
        "Start Outlook in safe mode: press Win + R and type outlook.exe /safe",
    ],
    "teams": [
        "Sign out of Teams and sign back in.",
        "Clear the Teams cache and restart Teams.",
        "Check if Teams works in the browser at teams.microsoft.com.",
    ],
    "onedrive": [
        "Check that OneDrive is running (cloud icon in the taskbar).",
        "Pause syncing and resume it.",
        "Make sure the file name has no unsupported characters.",
    ],
    "password": [
        "Use the self-service password reset portal.",
        "Make sure Caps Lock is off.",
        "If your account is locked, wait 15 minutes or contact IT.",
    ],
    "vpn": [
        "Disconnect and reconnect the VPN.",
        "Check your internet connection first.",
        "Restart the VPN client and your laptop.",
    ],
}


# ---------- Tool 1 ----------
def check_ticket_status(ticket_id: str) -> dict:
    """Returns the current status of an IT support ticket by its ID, like INC1002."""
    status = TICKETS.get(ticket_id.strip().upper())
    if status:
        return {"status": "success", "ticket_id": ticket_id.upper(), "details": status}
    return {"status": "error", "message": f"Ticket {ticket_id} was not found."}


# ---------- Tool 2 ----------
def get_troubleshooting_steps(app_name: str) -> dict:
    """Returns basic troubleshooting steps for an app or issue.
    Supported: outlook, teams, onedrive, password, vpn."""
    steps = KNOWLEDGE_BASE.get(app_name.strip().lower())
    if steps:
        return {"status": "success", "app": app_name, "steps": steps}
    return {
        "status": "error",
        "message": f"No steps found for '{app_name}'.",
        "supported": list(KNOWLEDGE_BASE.keys()),
    }


# ---------- Tool 3 ----------
def create_ticket(issue_summary: str, priority: str) -> dict:
    """Creates a new IT support ticket.
    priority must be Low, Medium, or High."""
    priority = priority.strip().capitalize()
    if priority not in ("Low", "Medium", "High"):
        priority = "Medium"
    new_id = f"INC{1001 + len(TICKETS)}"
    TICKETS[new_id] = f"New - {issue_summary} (Priority: {priority})"
    return {"status": "success", "ticket_id": new_id, "priority": priority}


# ---------- The agent ----------
root_agent = Agent(
    name="support_agent",
    model="gemini-3.5-flash",
    description="IT helpdesk assistant for Microsoft 365 issues.",
    instruction=(
        "You are a friendly IT helpdesk assistant for Microsoft 365 users.\n"
        "Rules:\n"
        "1. If the user asks about a ticket ID, use check_ticket_status.\n"
        "2. If the user reports a problem, first use get_troubleshooting_steps "
        "and share the steps clearly as a numbered list.\n"
        "3. If the steps don't fix it, offer to create a ticket. Ask for "
        "confirmation and priority (Low, Medium, High) before using create_ticket.\n"
        "4. Never invent ticket IDs or statuses. Only use what the tools return.\n"
        "5. Keep answers short and simple."
    ),
    tools=[check_ticket_status, get_troubleshooting_steps, create_ticket],
)
