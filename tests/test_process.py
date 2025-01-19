import unittest
from unittest.mock import patch

from okadminfinder.process import Process


class TestProcess(unittest.TestCase):
    @patch("okadminfinder.process.NetworkManager")
    def test_process_urls(self, mock_network_manager):
        process = Process(
            random_agent=False,
            proxy_url=None,
            use_tor=False,
            wordlist=None,
            dns=False,
            fuzz=False,
            output_path=None,
            clear_cache=False,
            timeout=10,
            num_pools=50,
            num_theads=16,
            num_retry=0,
        )
        process.process_urls("http://example.com")
        mock_network_manager.assert_called_once()


if __name__ == "__main__":
    unittest.main()
