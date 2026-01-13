# py_ai_refactor/display_session_info.py
import typer

from .constants.session_info import SessionInfo


def display_session_info(echo: bool = False):
    output = typer.echo if echo else print
    for info in SessionInfo:
        output(info.value)
