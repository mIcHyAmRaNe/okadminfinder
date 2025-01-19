#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class AppError(Exception):
    """Base class for all custom exceptions in the application."""

    pass


class UserAgentFileError(AppError):
    """Raised when the user-agent file is not found."""

    def __init__(self, file_path: str):
        super().__init__(f"User agents file not found: {file_path}")


class ProxyTorError(AppError):
    """Raised when both Proxy and Tor options are used together."""

    def __init__(self):
        super().__init__("Proxy and Tor options cannot be used together.")


class URLFormatError(AppError):
    """Raised when the provided URL has an invalid format."""

    def __init__(self, url: str):
        super().__init__(
            f"Invalid URL: {url}\nValid URL formats: http://example.com, https://example.com"
        )


class ProxyURLFormatError(AppError):
    """Raised when the provided proxy URL has an invalid format."""

    def __init__(self, proxy_url: str):
        super().__init__(f"Invalid proxy URL format: {proxy_url}")


class ProxyTypeError(AppError):
    """Raised when the proxy type is unsupported."""

    def __init__(self, proxy_type: str):
        super().__init__(f"Unsupported proxy type: {proxy_type}")


class RequestError(AppError):
    """Raised when a network request fails."""

    def __init__(self, message: str):
        super().__init__(message)


class DNSWithoutWordlistError(AppError):
    """Raised when the --dns option is used without the --wordlist option."""

    def __init__(self):
        super().__init__("The --dns option must be used with the --wordlist option.")


class FuzzAndDNSConflictError(AppError):
    """Raised when the --fuzz and --dns options are used together."""

    def __init__(self):
        super().__init__("The --fuzz and --dns options cannot be used together.")


class FilesWithoutFuzzError(AppError):
    """Raised when the --files option is used without the FUZZ method."""

    def __init__(self):
        super().__init__("The --files option can only be used with the FUZZ method.")


class FuzzURLFormatError(AppError):
    """Raised when the FUZZ keyword is not the last part of the URL."""

    def __init__(self):
        super().__init__("FUZZ must be the last part of the URL.")


class CustomParameterError(AppError):
    """Raised for invalid or missing command-line options."""

    def __init__(self, message: str):
        super().__init__(f"Missing parameter: {message}")
