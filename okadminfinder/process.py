#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from okadminfinder._utils import URLCreator
from okadminfinder.exceptions import (
    DNSWithoutWordlistError,
    FilesWithoutFuzzError,
    FuzzAndDNSConflictError,
    ProxyTorError,
    URLFormatError,
)
from okadminfinder.network import NetworkManager


class Process:
    def __init__(
        self,
        random_agent: bool,
        cookie: str,
        username: str,
        password: str,
        proxy_url: str,
        use_tor: bool,
        wordlist: str,
        dns: bool,
        fuzz: bool,
        files: str,
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
        Initialize the Process class with optional proxy settings.
        :param proxy_url: The proxy URL.
        :param proxy_type: The type of proxy (e.g., 'http').
        :param num_pools: The number of connection pools.
        """
        if proxy_url and use_tor:
            raise ProxyTorError()

        if use_tor:
            proxy_url = "socks5h://127.0.0.1:9050"

        if dns and not wordlist:
            raise DNSWithoutWordlistError()

        if fuzz and dns:
            raise FuzzAndDNSConflictError()

        if files and not fuzz:
            raise FilesWithoutFuzzError()

        self.url_creator = URLCreator(
            wordlist=wordlist, dns=dns, fuzz=fuzz, files=files
        )
        self.network_manager = NetworkManager(
            proxy_url,
            random_agent,
            cookie,
            username,
            password,
            status_codes,
            output_path,
            clear_cache,
            timeout,
            num_pools,
            num_threads,
            num_retry,
            delay,
        )

    @staticmethod
    def read_file(file_path: str) -> list:
        """
        Read a file containing a list of URLs.
        :param file_path: The path to the file containing URLs.
        :return: A list of URLs.
        """
        try:
            with open(file_path, "r") as file:
                urls = [line.strip() for line in file if line.strip()]
            return urls
        except FileNotFoundError:
            raise URLFormatError(file_path)
        except Exception as e:
            raise e

    def process_url(self, links: list) -> list:
        """
        Check the availability of a list of URLs.
        :param links: The list of URLs to check.
        :return: A list of available URLs.
        """
        try:
            return self.network_manager.check_urls(links)
        except KeyboardInterrupt:
            raise

    def process_urls(self, url: str, urls_file: str) -> None:
        """
        Process a single URL or a file containing a list of URLs.
        :param url: The single URL.
        :param urls_file: The path to the file containing URLs.
        :return: A list of available URLs.
        """
        links = []
        if urls_file:
            urls = self.read_file(urls_file)
        else:
            urls = [url]

        available_urls = []
        for base_url in urls:
            links.extend(self.url_creator.create_urls(base_url))

        return available_urls.extend(self.process_url(links))
