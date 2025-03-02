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

        # First try environment variable directly, then settings
        api_key = os.environ.get("ANTHROPIC_API_KEY") or settings.anthropic_api_key
        
        if not api_key:
            print("Missing Anthropic API key in settings and environment")
            print(f"API Key from settings exists: {bool(settings.anthropic_api_key)}")
            print(f"API Key from environment exists: {bool(os.environ.get('ANTHROPIC_API_KEY'))}")
            return None

        # Load work history for system context
        import json
        from pathlib import Path
        BASE_DIR = Path(__file__).parent
        with open(BASE_DIR / "data" / "work_history.json", "r", encoding="utf-8") as f:
            work_history = json.load(f)
        
        # Format work history as string for system prompt
        work_history_str = json.dumps(work_history, indent=2)
        
        # Create system prompt with work history
        system_prompt = (
            "Data about Chris Gutierrez's work history, skills, and experience are attached. "
            "When asked questions, assume that the question relates to Chris at work. "
            "If the question does not relate to Chris at work, then politely decline to answer.\n"
            "When possible, provide an example that answers the question. "
            "In the reply don't ask the questioner to look at a resume or other documentation, "
            "just answer the question to the best of your ability. "
            "You may provide work details and Chris's title information.\n\n"
            f"Work History: {work_history_str}"
        )

        client = Anthropic(api_key=api_key)

        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            temperature=0,
            system=system_prompt,
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