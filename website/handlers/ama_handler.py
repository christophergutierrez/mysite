
"""Handler for AMA questions using Anthropic Claude."""

import json
from website.askmeanything import chat_with_assistant  # Direct import
from starlette.responses import JSONResponse


async def handle_question(request):
    """Handle question by calling Claude API"""
    try:
        body = await request.body()
        data = json.loads(body)
        question = data.get("question")

        if not question:
            return JSONResponse({"response": "No question provided"})

        # Call the function directly
        response = chat_with_assistant(question)

        if response:
            return JSONResponse({"response": response[0]})  # Get first response
        return JSONResponse({"response": "No response received"})

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse({"response": f"Error: {str(e)}"})
