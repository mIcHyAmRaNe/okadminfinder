#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from okadminfinder.app import run


def main() -> object:
    """
    :rtype: object
    """
    try:
        return run()
    except KeyboardInterrupt:
        print("\n:boom: [bold red]Process interrupted by user[/bold red] :boom:")
        return


if __name__ == "__main__":
    main()
