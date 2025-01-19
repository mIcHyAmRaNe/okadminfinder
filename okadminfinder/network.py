#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from urllib.parse import urlparse

from rich import print
from rich.box import ROUNDED
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress
from urllib3 import PoolManager, ProxyManager
from urllib3 import __version__ as urllib3_version
from urllib3.contrib.socks import SOCKSProxyManager
from urllib3.exceptions import ConnectTimeoutError, HTTPError, MaxRetryError, ProxyError
from urllib3.util import Retry, Timeout

from okadminfinder._utils import UserAgent
from okadminfinder.cache import (
    disable_cache,
    invalidate_all_cache,
    memoize_if_cache_enabled,
)
from okadminfinder.exceptions import ProxyTypeError, ProxyURLFormatError


class NetworkManager:
    def __init__(
        self,
        proxy_url: str,
        random_agent: bool,
        cookie: str,
        username: str,
        password: str,
        status_codes: str,
        output_path: str,
        clear_cache: bool,
        timeout: int,
        num_pools: int,
        num_threads: int,
        num_retry: int,
        delay: float,
    ):
        """
        Initialize the NetworkManager class with optional proxy settings.
        :param proxy_url: The proxy URL.
        :param proxy_type: The type of proxy (e.g., 'http', 'https', 'socks5').
        :param num_pools: The number of connection pools.
        """
        self.user_agent = UserAgent()
        self.random_agent = random_agent
        self.cookie = cookie
        self.username = username
        self.password = password
        self.headers = self.get_default_headers()
        self.proxy_url = proxy_url
        self.status_codes = self.parse_status_codes(status_codes)
        self.output_path = output_path
        self.timeout = timeout
        self.num_pools = num_pools
        self.threads = num_threads
        self.num_retry = num_retry
        self.delay = delay
        self.http_manager = self.create_http_manager()
        self.available_urls = set()  # Use a set to store unique URLs
        self.executor = ThreadPoolExecutor(max_workers=self.threads)

        if clear_cache:
            invalidate_all_cache()
            disable_cache()
            print(
                ":anger: [bold yellow]Info: Cache cleared and disabled successfully.[/bold yellow] :anger:"
            )

    def get_default_headers(self):
        """
        Get the default headers for HTTP requests.
        :return: A dictionary of default headers.
        """
        headers = {
            "User-Agent": (
                self.user_agent.get_user_agent()
                if self.random_agent
                else f"urllib3/{urllib3_version}"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Sec-GPC": "1",
        }
        if self.cookie:
            headers["Cookie"] = self.cookie
        if self.username and self.password:
            headers["Authorization"] = f"Basic {self._encode_credentials()}"
        return headers

    def _encode_credentials(self) -> str:
        credentials = f"{self.username}:{self.password}"
        return base64.b64encode(credentials.encode()).decode()

    def set_timeout(self):
        return Timeout(total=self.timeout)

    def retry_strategy(self):
        return Retry(
            total=self.num_retry,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
        )

    def create_http_manager(self):
        """
        Create an HTTP manager (either ProxyManager, SOCKSProxyManager, or PoolManager) based on proxy settings.
        :return: An instance of urllib3.ProxyManager, urllib3.contrib.socks.SOCKSProxyManager, or urllib3.PoolManager.
        """
        if self.proxy_url:
            proxy_type, proxy_ip_port = self.parse_proxy_url(self.proxy_url)
            if proxy_type in ["socks4a", "socks5h"]:
                return SOCKSProxyManager(
                    proxy_url=self.proxy_url,
                    headers=self.headers,
                    timeout=self.set_timeout(),
                    num_pools=self.num_pools,
                    retries=self.retry_strategy(),
                    maxsize=self.threads,
                    block=True,
                )
            elif proxy_type in ["socks4", "socks5"]:
                proxy_type = self.transform_socks_type(proxy_type)
                transformed_proxy_url = f"{proxy_type}://{proxy_ip_port}"
                return SOCKSProxyManager(
                    proxy_url=transformed_proxy_url,
                    headers=self.headers,
                    timeout=self.set_timeout(),
                    num_pools=self.num_pools,
                    retries=self.retry_strategy(),
                    maxsize=self.threads,
                    block=True,
                )
            elif proxy_type in ["http", "https"]:
                return ProxyManager(
                    proxy_url=self.proxy_url,
                    proxy_headers=self.get_proxy_headers(),
                    headers=self.headers,
                    timeout=self.set_timeout(),
                    num_pools=self.num_pools,
                    retries=self.retry_strategy(),
                    maxsize=self.threads,
                    block=True,
                )
            else:
                raise ProxyTypeError(proxy_type)
        else:
            return PoolManager(
                headers=self.headers,
                timeout=self.set_timeout(),
                num_pools=self.num_pools,
                retries=self.retry_strategy(),
                maxsize=self.threads,
                block=True,
            )

    @staticmethod
    def parse_proxy_url(proxy_url: str):
        """
        Parse the proxy URL to extract the scheme and IP:port.
        :param proxy_url: The proxy URL.
        :return: A tuple containing the proxy type and IP:port.
        """
        parsed_url = urlparse(proxy_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ProxyURLFormatError(proxy_url)
        return parsed_url.scheme, parsed_url.netloc

    @staticmethod
    def transform_socks_type(proxy_type: str):
        """
        Transform socks4 to socks4a and socks5 to socks5h.
        :param proxy_type: The proxy type.
        :return: The transformed proxy type.
        """
        if proxy_type == "socks4":
            return "socks4a"
        elif proxy_type == "socks5":
            return "socks5h"
        return proxy_type

    @staticmethod
    def get_proxy_headers():
        """
        Get the proxy headers for HTTP requests.
        :return: A dictionary of proxy headers.
        """
        return {"Proxy-Authorization": "Basic base64encodedcredentials"}

    @staticmethod
    def parse_status_codes(status_codes_str: str) -> set:
        valid_status_codes = set()
        for part in status_codes_str.split(","):
            if "-" in part:
                start, end = map(int, part.split("-"))
                valid_status_codes.update(range(start, end + 1))
            else:
                valid_status_codes.add(int(part))
        return valid_status_codes

    def request(self, method: str, url: str, **kwargs):
        """
        Make an HTTP request using the appropriate manager.
        :param method: The HTTP method (e.g., 'GET', 'POST').
        :param url: The URL to request.
        :param kwargs: Additional keyword arguments for the request.
        :return: The HTTP response.
        """
        return self.http_manager.request(method, url, **kwargs)

    @memoize_if_cache_enabled
    def check_url(self, url: str) -> bool:
        """
        Check the availability of a URL.
        :param url: The URL to check.
        :return: True if the URL is available, False otherwise.
        """
        try:
            if self.delay > 0:
                sleep(self.delay)
            resp = self.request("GET", url)
            # print(f"[{resp.status}] {url}")
            if resp.status in self.status_codes:
                return True
        except (
            ConnectTimeoutError,
            MaxRetryError,
            HTTPError,
            ProxyError,
        ):
            return False

    def check_urls(self, paths: list) -> list:
        """
        Check the availability of a list of URLs with multithreading and a progress bar.
        :param paths: The list of URLs to check.
        :return: A list of available URLs.
        """

        # Initialize the progress bar
        progress = Progress()
        task = progress.add_task(" [cyan]Checking URLs...", total=len(paths))
        try:
            with Live(progress, auto_refresh=True, refresh_per_second=10) as live:
                # Submit all tasks to the executor
                futures = {
                    self.executor.submit(self.check_url, path): path for path in paths
                }

                # Process tasks as they are completed
                for future in as_completed(futures):
                    path = futures[future]
                    if future.result():  # Check if the URL is valid
                        self.available_urls.add(path)

                    # Update the progress bar
                    progress.update(task, advance=1)

                    # Dynamically update the live display
                    if self.available_urls:
                        found_urls_display = "\n".join(self.available_urls)
                        live.update(
                            Group(
                                progress,
                                Panel(
                                    found_urls_display,
                                    box=ROUNDED,
                                    title="[bold chartreuse3]Found URLs[/bold chartreuse3]",
                                    subtitle="[dark_sea_green4]Thank you for using okadminfinder![/dark_sea_green4]",
                                    expand=False,
                                    highlight=True,
                                    border_style="dark_green",
                                    padding=(0, 10),
                                ),
                            )
                        )
            if self.output_path:
                self.save_results(list(self.available_urls), self.output_path)
        except KeyboardInterrupt:
            # Handle user interruption gracefully
            for future in futures:
                future.cancel()
            self.executor.shutdown(wait=False)
            progress.stop()
            print("\n:boom: [bold red]Process interrupted by user[/bold red] :boom:")

        return list(self.available_urls)

    @staticmethod
    def save_results(urls: list, output_path: str):
        """
        Save the list of URLs to a file.
        :param urls: The list of URLs to save.
        :param output_path: The path to the output file.
        """
        with open(output_path, "w") as f:
            for url in urls:
                f.write(url + "\n")
        print(
            f":boom: [bold yellow]Results written to {output_path}[/bold yellow] :boom:"
        )
