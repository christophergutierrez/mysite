# Personal Website

A FastHTML-based personal website featuring a dynamic experience timeline, blog redirects, and an AI-powered Ask Me Anything section using OpenAI's Assistant API.

## Features

- **Home Page**: Article about AI in software development
- **Experience Timeline**: Interactive visualization of professional history
- **Ask Me Anything**: AI-powered Q&A using OpenAI's Assistant
- **Blog**: Redirects to personal GitHub Pages blog
- **Static Asset Handling**: Images, CSS, and JavaScript management

## Requirements

- Python 3.8, 3.10, or 3.12
- OpenAI API key and Assistant ID
- Dependencies are managed through setup.py

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd website
```

2. Create a virtual environment:
```bash
conda create -n mysite python=3.12
conda activate mysite
```

3. Install the packages in development mode:
```bash
pip install -e .
```

4. Create a `.env` file in the root directory:
```bash
touch .env
```
The file should contain the following environment variables:
```bash
ENV=DEV
DEV_PORT=5000
PROD_PORT=8080
OPENAI_API_KEY=[your-api-key]
OPENAI_ASSISTANT_ID=[your-assistant-id]
```

5. Run the website:
```bash
python run.py
```

The website should now be running on `http://localhost:5000`.
