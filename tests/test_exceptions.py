import unittest

from okadminfinder.exceptions import (
    AppError,
    DNSWithoutWordlistError,
    FuzzAndDNSConflictError,
    ProxyTorError,
    ProxyTypeError,
    ProxyURLFormatError,
    RequestError,
    URLFormatError,
    UserAgentFileError,
)


class TestExceptions(unittest.TestCase):
    def test_app_error(self):
        with self.assertRaises(AppError):
            raise AppError("Test error")

    def test_user_agent_file_error(self):
        with self.assertRaises(UserAgentFileError):
            raise UserAgentFileError("test_file")

    def test_proxy_tor_error(self):
        with self.assertRaises(ProxyTorError):
            raise ProxyTorError()

    def test_url_format_error(self):
        with self.assertRaises(URLFormatError):
            raise URLFormatError("http://invalid_url")

    def test_proxy_url_format_error(self):
        with self.assertRaises(ProxyURLFormatError):
            raise ProxyURLFormatError("invalid_proxy")

    def test_proxy_type_error(self):
        with self.assertRaises(ProxyTypeError):
            raise ProxyTypeError("invalid_type")

    def test_request_error(self):
        with self.assertRaises(RequestError):
            raise RequestError("Request failed")

    def test_dns_without_wordlist_error(self):
        with self.assertRaises(DNSWithoutWordlistError):
            raise DNSWithoutWordlistError()

    def test_fuzz_and_dns_conflict_error(self):
        with self.assertRaises(FuzzAndDNSConflictError):
            raise FuzzAndDNSConflictError()


if __name__ == "__main__":
    unittest.main()
