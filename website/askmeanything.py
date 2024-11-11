"""Script to interact with OpenAI's Assistant API."""

import argparse
import time
from typing import Optional, List
from pathlib import Path
from openai import OpenAI
from website.config.settings import get_app_settings

def chat_with_assistant(user_message: str) -> Optional[List[str]]:
    """Send a message to OpenAI assistant and get responses."""
    try:
        # Get settings which includes OpenAI credentials
        settings = get_app_settings()
        
        if not settings.openai_api_key or not settings.openai_assistant_id:
            print("Missing OpenAI credentials in settings")
            return None

        # Create OpenAI client with API key from settings
        client = OpenAI(api_key=settings.openai_api_key)

        # Create a thread
        thread = client.beta.threads.create()

        # Add the message to the thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # Create and poll the run
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=settings.openai_assistant_id
        )

        # Poll for completion
        while True:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run.status == "completed":
                break
            if run.status in ["failed", "cancelled", "expired"]:
                raise ValueError(f"Run ended with status: {run.status}")
            time.sleep(1)

        # Retrieve and return messages
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        return [
            message.content[0].text.value
            for message in messages
            if message.role == "assistant"
        ]

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """Process command line arguments and run the chat assistant."""
    parser = argparse.ArgumentParser(description="Chat with OpenAI Assistant")
    parser.add_argument("message", type=str, help="Message to send to the assistant")
    args = parser.parse_args()

    responses = chat_with_assistant(args.message)
    if responses:
        for response in responses:
            print(response)

if __name__ == "__main__":
    main()
