#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

from rich.align import Align
from rich.color import Color
from rich.console import Console
from rich.text import Text

from okadminfinder.version import __creator__, __maintainer__, __version__


class Credit:
    @staticmethod
    def _apply_gradient(text, start_color, end_color):
        """
        Apply a gradient to the given text.

        Args:
            text (str): The text to style.
            start_color (str): Starting color in hex format (e.g., "#ff0000").
            end_color (str): Ending color in hex format (e.g., "#0000ff").
        """
        start = Color.parse(start_color).triplet
        end = Color.parse(end_color).triplet
        gradient = [
            (
                int(start[0] + (end[0] - start[0]) * i / len(text)),
                int(start[1] + (end[1] - start[1]) * i / len(text)),
                int(start[2] + (end[2] - start[2]) * i / len(text)),
            )
            for i in range(len(text))
        ]

        styled_text = Text()
        for char, color in zip(text, gradient):
            styled_text.append(char, style=f"rgb({color[0]},{color[1]},{color[2]})")
        return styled_text

    @contextmanager
    def set_credit(self):
        try:
            console = Console()
            credit_text = r"""
    ╔──────────────────────────────────────────────────────────────╗
    │    ___  _  __        _       _      ___ _         _          │
    │   / _ \| |/ /__ _ __| |_ __ (_)_ _ | __(_)_ _  __| |___ _ _  │
    │  | (_) | ' </ _` / _` | '  \| | ' \| _|| | ' \/ _` / -_) '_| │
    │   \___/|_|\_\__,_\__,_|_|_|_|_|_||_|_| |_|_||_\__,_\___|_|   │
    │                                                              │
    ╚──────────────────────────────────────────────────────────────╝"""
            version_info = f"    [bold]:green_heart: version {__version__} created by {__creator__} & recoded by {__maintainer__} :green_heart:[/bold]\n"
            gradient_text = self._apply_gradient(credit_text, "#4AC29A", "#BDFFF3")
            credit = Align(gradient_text, align="left", vertical="top")
            version_credit = Align(version_info, align="left", vertical="top")
            console.print(credit)
            console.print(version_credit)
            yield
        finally:
            pass
