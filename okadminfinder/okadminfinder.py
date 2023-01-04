#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

import trio
from trio import TrioDeprecationWarning
import warnings

from okadminfinder import _classes


def main():
    classes = _classes.okadminfinder()
    warnings.filterwarnings(action="ignore", category=TrioDeprecationWarning)

    with classes.credit():
        parser = argparse.ArgumentParser(
            formatter_class=lambda prog: argparse.HelpFormatter(
                prog, max_help_position=30, width=90
            )
        )
        parser.add_argument(
            "-u",
            "--url",
            default=False,
            help="Target URL (e.g. 'www.example.com' or 'example.com')",
        )
        parser.add_argument(
            "-t",
            "--tor",
            action="store_true",
            default=False,
            help="Use Tor anonymity network",
        )
        parser.add_argument(
            "-p",
            "--proxy",
            default=False,
            help="""To use an HTTP(S) proxy (e.g '127.0.0.1:8080')
                    To use an SOCKS(4/5) proxy (e.g 'socks5://127.0.0.1:8080'""",
        )
        parser.add_argument(
            "-r",
            "--random-agent",
            action="store_true",
            default=False,
            dest="rand",
            help="Use randomly selected User-Agent",
        )
        if len(sys.argv) <= 1:
            parser.print_usage()
            sys.exit(2)
        else:
            args = parser.parse_args()

            # user-agent
            if args.rand:
                headers = classes.get_agents()
            else:
                headers = None

            # proxy
            if args.proxy:
                if args.url is False:
                    parser.print_usage()
                    quit(0)
                else:
                    if str(args.proxy)[0:5] == "socks":
                        prox = str(args.proxy)
                        classes.proxy(prox, headers)
                        proxies = classes.proxy(prox, headers)

                    else:
                        prox = str(args.proxy)
                        prox = {
                            "http://": f"http://{prox}",
                            "https://": f"http://{prox}",
                        }
                        classes.proxy(prox, headers)
                        proxies = classes.proxy(prox, headers)

            else:
                proxies = None

            # url
            if args.url:
                website = args.url
                trio.run(classes.url, website, headers, proxies)


if __name__ == "__main__":
    main()
