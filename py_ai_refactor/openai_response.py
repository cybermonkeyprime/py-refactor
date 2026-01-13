# py_ai_refactor/openai_response.py
from openai import OpenAI

from .configuration import api_key, model_name
from .initial_prompt_build import build_initial_prompt
from .log_setup import logger

client = OpenAI(api_key=api_key)


# === GPT Integration ===
def get_openai_response(code: str) -> str:
    logger.debug(f"get_openai_response(): {model_name=}")
    logger.debug(f"get_openai_response(): {code.strip()=}")
    response = client.chat.completions.create(
        model=model_name,
        temperature=0.3,
        messages=build_initial_prompt(code),
    )
    logger.debug(f"get_openai_response(): {response=}")
    return response.choices[0].message.content or ""
