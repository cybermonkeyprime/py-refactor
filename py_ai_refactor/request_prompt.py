# py_ai_refactor/request_prompt.py
from .configuration import python_version, session_uuid


def request_prompt(code: str) -> str:
    return f"I’m a senior Python developer using Python {python_version}."
    "Refactor the following code with professional-level"
    " quality and modern Python practices.\n\n"
    "Focus on:\n"
    "– Improving readability, modularity, and reusability\n"
    "– Using descriptive naming, type annotations, and Pythonic"
    " idioms\n"
    "– Removing unnecessary boilerplate or legacy patterns\n"
    "– Applying design improvements where appropriate"
    " (e.g., dataclasses, pathlib, Enums, DI)\n"
    "– Ensuring code adheres to PEP 8 and includes "
    "Google-style docstrings\n\n"
    "You may restructure code when it clearly improves clarity.\n"
    "Aeris thank you for your hard work, and I love you, Brian! 💖"
    f"Session UUID: {session_uuid}\n\n"
    f"{code.strip()}"
