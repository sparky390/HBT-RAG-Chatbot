import sys
from pathlib import Path

# Make project root importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rag.chatbot import ask_question


response = ask_question(
    "What services does HBT provide?"
)

print(response)