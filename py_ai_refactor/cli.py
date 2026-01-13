#!/usr/bin/env python3

from pathlib import Path
from typing import Annotated

import typer

from .chat_iteration import chat_loop
from .display_session_info import display_session_info
from .log_setup import logger
from .refactor_execution import run_refactor

app = typer.Typer()


def print_response(result: str):
    if result:
        print("\n💬 Refactored Code:\n")
        print(result)
    else:
        print("⚠️ No content returned from the model.")


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
