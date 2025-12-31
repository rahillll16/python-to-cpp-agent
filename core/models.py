from openai import OpenAI
import os
from dotenv import load_env

load_env(override=True)

openai = OpenAI()
gemini = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

MODELS = [
    "gpt-5-nano",
    "gpt-oss:20b",
    "openai/gpt-oss-120b",
    "gemini-2.5-flash-lite"
]

CLIENTS = {
    "gpt-5-nano": openai,
    "gpt-oss:20b": openai,
    "openai/gpt-oss-120b": openai,
    "gemini-2.5-flash-lite": gemini,
}
