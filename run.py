import uvicorn
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path(".") / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    print("Note: .env file not found. Environment variables should be set manually.")
    print("You can copy .env.example to .env and fill in your Braintrust API key.")

if __name__ == "__main__":
    # Run the FastAPI application using Uvicorn
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True  # Enable auto-reload for development
    ) 