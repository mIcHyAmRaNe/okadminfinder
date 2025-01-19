#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import re

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from typer import Exit
from typer.models import OptionInfo

console = Console()

STYLE_OPTION = "bold cyan"
STYLE_SWITCH = "bold green"
STYLE_ERRORS_PANEL_BORDER = "red"
ERRORS_PANEL_TITLE = "[red]Error[/red]"
ALIGN_ERRORS_PANEL = "left"


def detect_options_from_typer(app):
    """
    Detects all options from the Typer app and returns a dictionary with
    options and their corresponding styles (color).

    Args:
        app (Typer): The Typer app instance.

    Returns:
        dict: A dictionary where keys are option names (with `--` or `-`)
              and values are their respective styles (color).
    """
    options = {}

    for command_info in app.registered_commands:
        callback = command_info.callback
        sig = inspect.signature(callback)
        for param in sig.parameters.values():
            option_info = param.default
            if isinstance(option_info, OptionInfo):
                for opt in option_info.param_decls:
                    color = STYLE_OPTION if opt.startswith("--") else STYLE_SWITCH
                    options[opt] = color

    return options


def custom_error_handler(app, message: str):
    """
    Displays a styled error message dynamically, highlighting options declared in the Typer app.

    Args:
        app (Typer): The Typer app instance to extract options from.
        message (str): The main error message.
    """
    # Detect options dynamically from Typer
    option_styles = detect_options_from_typer(app)

    text = Text(message)

    # Highlight each option dynamically based on the extracted styles
    for option, style in option_styles.items():
        text.highlight_regex(rf"(?<![\w\-]){re.escape(option)}(?![\w\-])", style=style)

    # Print the styled panel
    console.print(
        Panel(
            text,
            border_style=STYLE_ERRORS_PANEL_BORDER,
            title=ERRORS_PANEL_TITLE,
            title_align=ALIGN_ERRORS_PANEL,
        )
    )
    raise Exit(code=1)
