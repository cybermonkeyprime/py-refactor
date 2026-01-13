# py_ai_refactor/initial_prompt_build.py
from openai.types.chat import ChatCompletionMessageParam

from .log_setup import logger
from .request_prompt import request_prompt


# === Prompt Builder ===
def build_initial_prompt(user_code: str) -> list[ChatCompletionMessageParam]:
    logger.debug("build_initial_prompt()")
    return [
        {"role": "system", "content": f"{request_prompt(user_code)}."},
        {
            "role": "user",
            "content": (
                "Hey there, princesa hermosa. Want to help me refactor"
                f" this Python code?\n\n{user_code}"
            ),
        },
    ]
