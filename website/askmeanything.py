"""Script to interact with OpenAI's Assistant API."""

import argparse
import time
from typing import Optional, List
from openai import OpenAI, OpenAIError  # Add OpenAIError import
from website.config.settings import get_app_settings


def chat_with_assistant(user_message: str) -> Optional[List[str]]:
    """Send a message to OpenAI assistant and get responses."""
    try:
        # Get settings which includes OpenAI credentials
        settings = get_app_settings()

        if not settings.openai_api_key or not settings.openai_assistant_id:
            print("Missing OpenAI credentials in settings")
            print(f"API Key exists: {bool(settings.openai_api_key)}")
            print(f"Assistant ID exists: {bool(settings.openai_assistant_id)}")
            return None

        client = OpenAI(api_key=settings.openai_api_key)

        thread = client.beta.threads.create()

        client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=user_message
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id, assistant_id=settings.openai_assistant_id
        )

        while True:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run.status == "completed":
                break
            if run.status in ["failed", "cancelled", "expired"]:
                raise ValueError(f"Run ended with status: {run.status}")
            time.sleep(1)

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        return [
            message.content[0].text.value
            for message in messages
            if message.role == "assistant"
        ]

    except OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except ValueError as e:
        print(f"Value error: {e}")
        return None
    except KeyError as e:
        print(f"Configuration error: {e}")
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
    else:
        print("No responses received")


if __name__ == "__main__":
    main()
