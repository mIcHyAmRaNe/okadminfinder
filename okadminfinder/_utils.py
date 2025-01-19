#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib.resources import open_text
from random import choice
from urllib.parse import urlsplit

from yaml import safe_load

from okadminfinder.exceptions import (
    FuzzURLFormatError,
    URLFormatError,
    UserAgentFileError,
)


class UserAgent:
    """
    Manage user-agents
    """

    def __init__(
        self,
        ua_file: str = r"user-agents.yml",
    ):
        """
        Initialize the UserAgent class with a file containing user-agents.
        :param ua_file: Path to the user-agents YAML file.
        """
        try:
            with open_text("okadminfinder.assets", ua_file, encoding="utf-8") as file:
                self.user_agents = safe_load(file)
        except FileNotFoundError as e:
            raise UserAgentFileError(ua_file) from e

    def get_user_agent(self) -> str:
        """
        Return a random user-agent from the loaded user-agents.
        :return: A random user-agent string.
        """
        rua = choice(self.user_agents)
        return rua.rstrip()


class URLCreator:
    """
    Manage and verify URLs of admin panel
    """

    def __init__(
        self,
        wordlist: str,
        dns: bool,
        fuzz: bool,
        files: str,
        apl_file: str = r"admin-panel_links.yml",
    ):
        """
        Initialize the URLCreator class with a file containing admin panel links.
        :param apl_file: Path to the admin panel links YAML file.
        """
        self.paths = None
        self.dns = dns
        self.fuzz = fuzz
        self.files = files.split(",") if files else []
        if wordlist:
            self.load_wordlist(wordlist)
        else:
            self.load_default_links(apl_file)

    def load_wordlist(self, wordlist: str):
        try:
            with open(wordlist, "r", encoding="utf-8") as file:
                self.paths = [
                    line.strip() for line in file if not line.strip().startswith("#")
                ]
        except FileNotFoundError as e:
            raise URLFormatError(wordlist) from e

    def load_default_links(self, apl_file: str):
        try:
            with open_text("okadminfinder.assets", apl_file, encoding="utf-8") as file:
                self.paths = safe_load(file)
        except FileNotFoundError as e:
            raise URLFormatError(apl_file) from e

    @staticmethod
    def create_url(base_url: str, path: str, dns: bool = False) -> str:
        """
        Generate a URL using base URL + a path.
        :param base_url: The base URL.
        :param path: The path to append to the base URL.
        :param dns: Whether to use DNS mode.
        :return: The constructed URL.
        """
        # Validate and parse the base URL
        try:
            if not base_url.startswith(("http://", "https://")):
                raise URLFormatError(base_url)

            scheme, netloc, _, _, _ = urlsplit(base_url)
        except Exception:
            raise URLFormatError(base_url)

        # Handle case where the host starts with 'www.'
        host = netloc.split(":")[0]  # Extract the hostname
        if host.startswith("www."):
            host = host.replace("www.", "")

        # Extract the port if present
        port = netloc.split(":")[1] if ":" in netloc else ""

        # Reconstruct the full netloc (host + optional port)
        full_netloc = f"{host}:{port}" if port else host

        if dns:
            return f"{scheme}://{path}.{full_netloc}"
        else:
            return f"{scheme}://{path.format(full_netloc)}"

    def create_urls(self, base_url: str) -> list[str]:
        """
        Generate a list of URLs from paths.
        :param base_url: The base URL.
        :return: A list of constructed URLs.
        """
        if self.fuzz:
            # Remove {} placeholders from the default dictionary entries
            cleaned_paths = [
                path.replace("{}.", "").replace(".{}", "").replace("{}/", "")
                for path in self.paths
            ]
            if base_url.endswith("FUZZ"):
                base_url = base_url.replace("FUZZ", "{}")
                urls = [base_url.format(path) for path in cleaned_paths]
                if self.files:
                    extended_urls = []
                    for url in urls:
                        extended_urls.append(url)  # Add the directory URL
                        for file_ext in self.files:
                            extended_urls.append(f"{url}.{file_ext}")
                    return extended_urls
                return urls
            else:
                raise FuzzURLFormatError()
        elif self.dns:
            return [self.create_url(base_url, path, self.dns) for path in self.paths]
        else:
            return [self.create_url(base_url, path) for path in self.paths]
