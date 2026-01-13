# py_ai_refactor/refactor_execution.py
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from .log_setup import logger
from .openai_response import get_openai_response

console = Console()


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
