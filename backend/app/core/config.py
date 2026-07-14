from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError(f"OPENAI_API_KEY not found. Looked for .env at {env_path}")

IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY")
if not IMAGEKIT_PRIVATE_KEY:
    raise RuntimeError(f"IMAGEKIT_PRIVATE_KEY not found. Looked for .env at {env_path}")

IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY")
if not IMAGEKIT_PUBLIC_KEY:
    raise RuntimeError(f"IMAGEKIT_PUBLIC_KEY not found. Looked for .env at {env_path}")

IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT")
if not IMAGEKIT_URL_ENDPOINT:
    raise RuntimeError(f"IMAGEKIT_URL_ENDPOINT not found. Looked for .env at {env_path}")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(f"DATABASE_URL not found. Looked for .env at {env_path}")