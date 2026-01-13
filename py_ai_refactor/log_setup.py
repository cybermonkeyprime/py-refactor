# py_ai_refactor/log_setup.py
import sys

from loguru import logger

logger.remove()  # Remove default handler
logger.add(sys.stderr, level="INFO")  # Only show INFO and above
