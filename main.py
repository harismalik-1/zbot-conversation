import os
import dotenv
import asyncio
from .voice.voice import Voice

dotenv.load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "default")

voice = Voice(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    config=None,
)

@voice.event("ready")
async def on_ready():
    print("Voice system is ready")

if __name__ == "__main__":
    asyncio.run(voice.run())
