"""
agent_demo.py

A modular demo script that simulates basic AI agent behavior using task modules.
Author: Gordan | AI Whisperer
"""

def rephrase(text):
    return "Kindly reformulate this statement to maintain a professional tone."

def summarize(text):
    return "Summary: " + text.split('.')[0] + "..."

def classify(text):
    return "This appears to be a request for rephrasing."

# Simulated agent router
def agent_router(user_input):
    if "rephrase" in user_input.lower() or "professional" in user_input.lower():
        module = "rephrase"
        result = rephrase(user_input)
    elif "summarize" in user_input.lower():
        module = "summarize"
        result = summarize(user_input)
    elif "classify" in user_input.lower():
        module = "classify"
        result = classify(user_input)
    else:
        module = "unknown"
        result = "Sorry, I couldn't understand the task."
    
    return module, result

if __name__ == "__main__":
    print("=== Modular Agent Demo ===")
    user_input = input("Enter your request: ")
    module, output = agent_router(user_input)
    print(f"Module used: {module}")
    print(f"Agent response: {output}")
