#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich import print
from typer import Abort, Option, Typer

from okadminfinder.credit import Credit
from okadminfinder.errors_handler import custom_error_handler, detect_options_from_typer
from okadminfinder.logging import LoggingConfig
from okadminfinder.process import Process

app = Typer(help="Admin panel finder application.", no_args_is_help=True)

credit = Credit()


@app.command()
def main(
    url: str = Option(
        None,
        "--url",
        "-u",
        help="Target URL (e.g. http://example.com or 'https://example.com')",
    ),
    urls_file: str = Option(
        None,
        "--urls-file",
        "-U",
        help="File containing a list of URLs to scan",
    ),
    random_agent: bool = Option(
        False, "--random-agent", "-r", help="Use random user agent"
    ),
    proxy: str = Option(
        None, "--proxy", "-p", help="Proxy address (e.g. '127.0.0.1:8080')"
    ),
    tor: bool = Option(False, "--tor", "-t", help="Use Tor anonymity network"),
    wordlist: str = Option(
        None, "--wordlist", "-w", help="Path to the custom wordlist file"
    ),
    dns: bool = Option(False, "--dns", "-d", help="Use DNS mode for wordlist"),
    fuzz: bool = Option(
        False,
        "--fuzz",
        "-F",
        help="Use fuzzing mode (e.g. '-u https://example.com/road/to/FUZZ')",
    ),
    files: str = Option(
        None, "--files", "-f", help="File extensions to search for (e.g. 'php,txt,js')"
    ),
    status_codes: str = Option(
        "200,301,401,500",
        "--status-codes",
        "-s",
        help="Comma-separated list of valid HTTP status codes or ranges (e.g. '200,301,401' or '200-399,501')",
    ),
    cookie: str = Option(
        None,
        "--cookie",
        "-C",
        help="Set custom cookies (e.g. 'session=f3efe9db; id=30')",
    ),
    username: str = Option(
        None, "--username", "-I", help="Identifier for authentication"
    ),
    password: str = Option(
        None, "--password", "-P", help="Password for authentication"
    ),
    output: str = Option(
        None, "--output", "-o", help="Output file path (e.g. 'output.txt')"
    ),
    clear_cache: bool = Option(
        False, "--clear-cache", "-c", help="Clear and disable the cache"
    ),
    timeout: int = Option(10, "--timeout", "-T", help="Timeout in seconds"),
    num_pools: int = Option(
        50, "--num-pools", "-k", help="Number of connection pools to use"
    ),
    threads: int = Option(16, "--threads", "-j", help="Number of threads and maxsize"),
    retry: int = Option(0, "--retry", "-R", help="Number of retries"),
    delay: float = Option(
        0.0, "--delay", "-l", help="Delay (latency) in seconds between requests"
    ),
    debug: bool = Option(False, "--debug", "-D", help="Enable debug logging"),
):
    # Validate URL and file options
    if not url and not urls_file:
        custom_error_handler(
            app, "Missing option '--url' / '-u' or '--urls-file' / '-U'."
        )
    if url and urls_file:
        custom_error_handler(
            app, "You cannot provide both --url (-u) and --urls-file (-U)."
        )

    try:
        process = Process(
            random_agent=random_agent,
            proxy_url=proxy,
            use_tor=tor,
            wordlist=wordlist,
            dns=dns,
            fuzz=fuzz or (url and "FUZZ" in url),
            files=files,
            status_codes=status_codes,
            cookie=cookie,
            username=username,
            password=password,
            output_path=output,
            clear_cache=clear_cache,
            timeout=timeout,
            num_pools=num_pools,
            num_threads=threads,
            num_retry=retry,
            delay=delay,
        )

        # configure logging based on debug flag
        LoggingConfig.configure_logging(debug)

        # run process_urls
        process.process_urls(url, urls_file)

    except Exception as e:
        if debug:
            raise e
        else:
            print(f"\n :x: [bold red]Error: {e}[/bold red]")
            Abort()


def run():
    try:
        with credit.set_credit():
            detect_options_from_typer(app)
            app()
    except KeyboardInterrupt:
        print("\n:boom: [bold red]Process interrupted by user[/bold red] :boom:")
        Abort()
