"""Script to interact with Anthropic's Claude API."""

import argparse
from typing import Optional, List
from anthropic import Anthropic
from website.config.settings import get_app_settings


def chat_with_assistant(user_message: str) -> Optional[List[str]]:
    """Send a message to Claude 3.5 Haiku and get responses."""
    try:
        # Get settings which includes Anthropic credentials
        settings = get_app_settings()

        if not settings.anthropic_api_key:
            print("Missing Anthropic API key in settings")
            print(f"API Key exists: {bool(settings.anthropic_api_key)}")
            return None

        client = Anthropic(api_key=settings.anthropic_api_key)

        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        # Return the assistant's response
        return [message.content[0].text]

    except Exception as e:
        print(f"Anthropic API error: {e}")
        return None


def main():
    """Process command line arguments and run the chat assistant."""
    parser = argparse.ArgumentParser(description="Chat with Claude 3.5 Haiku")
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