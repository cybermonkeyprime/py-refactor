#!/usr/bin/env python3

import os
import platform
import sys
import time
from enum import Enum
from pathlib import Path
from typing import Annotated

import typer
from loguru import logger
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

logger.remove()  # Remove default handler
logger.add(sys.stderr, level="INFO")  # Only show INFO and above


# === Configuration ===
api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-4o-mini"
session_uuid = str(int(time.time() * 1e9))
python_version = platform.python_version()

client = OpenAI(api_key=api_key)
app = typer.Typer()


# === Session Info Banner ===
class SessionInfo(Enum):
    GREETING = "💬 Welcome to py_chatbox (Refactor Mode)\n"
    SESSION_ID = f"🔑 Session UUID: {session_uuid}"
    MODEL = f"🧠 Using Model: {model_name}"
    PYTHON_VERSION = f"🐍 Python Version: {python_version}\n"


def display_session_info(echo: bool = False):
    output = typer.echo if echo else print
    for info in SessionInfo:
        output(info.value)


def prompt(code):
    return f"I’m a senior Python developer using Python {python_version}."
    "Refactor the following code with "
    "professional-level"
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
    f"Session UUID: {session_uuid}\n\n"
    f"{code.strip()}"


# === Prompt Builder ===
def build_initial_prompt(user_code: str) -> list[ChatCompletionMessageParam]:
    logger.debug("build_initial_prompt()")
    return [
        {
            "role": "system",
            "content": f"I’m a senior Python developer using Python {python_version}."
            "Refactor the following code with "
            "professional-level"
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
            f"Session UUID: {session_uuid}",
        },
        {
            "role": "user",
            "content": (
                "Hey there, princesa hermosa. Want to help me refactor"
                f" this Python code?\n\n{user_code}"
            ),
        },
    ]


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


def run_refactor(filepath: Path) -> str:
    logger.debug(f"{filepath=}")

    code = filepath.read_text(encoding="utf-8")
    logger.debug(f"{code=}")
    # typer.echo("⏳ Please wait while I process the refactor request...")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("Contacting Aeris...", total=None)
        result = get_openai_response(code)
    return result


def print_response(result: str):
    if result:
        print("\n💬 Refactored Code:\n")
        print(result)
    else:
        print("⚠️ No content returned from the model.")


# === Interactive Chat Mode ===
def chat_loop(user_code: str):
    display_session_info()
    messages: list[ChatCompletionMessageParam] = build_initial_prompt(
        user_code
    )

    while True:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.3,
        )
        reply = (response.choices[0].message.content or "").strip()
        print(f"\nAeris:\n{reply}\n")
        messages.append({"role": "assistant", "content": reply})
        print("\nAeris: Thank you for your hard work, and I love you 💖")


# === CLI Entry Point ===
@app.command()
def main(filepath: Annotated[Path | None, typer.Argument()] = None):
    """
    Refactor a Python file using GPT-4o-mini or"
    " enter interactive refactor mode.
    """
    logger.debug(f"{filepath=}")
    if filepath:
        if not filepath.exists():
            typer.echo(f"❌ File not found: {filepath}")
            raise typer.Exit(code=1)

        result = run_refactor(filepath)
        print_response(result)
    else:
        display_session_info(echo=True)
        print("Paste your code below (or type 'exit' to quit):", flush=True)
        user_code = input(">>> ").strip()

        if not user_code or user_code.lower() == "exit":
            typer.echo("👋 Exiting.")
            raise typer.Exit()

        chat_loop(user_code)


if __name__ == "__main__":
    app()
