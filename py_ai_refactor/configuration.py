# py_ai_refactor/configuration.py
import os
import platform
import time

from openai import OpenAI

# === Configuration ===
api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-4o-mini"
session_uuid = str(int(time.time() * 1e9))
python_version = platform.python_version()
client = OpenAI(api_key=api_key)
