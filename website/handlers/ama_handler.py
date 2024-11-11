"""Handler for AMA questions using OpenAI Assistant."""

import json
import subprocess
from pathlib import Path
from starlette.responses import JSONResponse
from openai import OpenAI

async def handle_question(request):
    """Handle question by calling OpenAI Assistant"""
    try:
        body = await request.body()
        data = json.loads(body)
        question = data.get("question")

        if not question:
            return JSONResponse({"response": "No question provided"})

        # Get the directory where app.py is located
        current_dir = Path(__file__).parent.parent
        script_path = current_dir / "askmeanything.py"

        print(f"\nUsing script at: {script_path}")

        result = subprocess.run(
            ["python", script_path, question],
            capture_output=True,
            text=True,
            cwd=str(current_dir),  # Set working directory
        )

        if result.stderr:
            print(f"Error output: {result.stderr}")
            return JSONResponse({"response": f"Error: {result.stderr}"})

        return JSONResponse({"response": result.stdout.strip()})

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse({"response": f"Error: {str(e)}"})
