# py_ai_refactor/constants/session_info.py
from enum import Enum

from ..configuration import model_name, python_version, session_uuid


# === Session Info Banner ===
class SessionInfo(Enum):
    GREETING = "💬 Welcome to py_chatbox (Refactor Mode)\n"
    SESSION_ID = f"🔑 Session UUID: {session_uuid}"
    MODEL = f"🧠 Using Model: {model_name}"
    PYTHON_VERSION = f"🐍 Python Version: {python_version}\n"
