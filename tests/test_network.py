import unittest
from unittest.mock import patch

from okadminfinder.network import NetworkManager


class TestNetworkManager(unittest.TestCase):
    @patch("okadminfinder.network.PoolManager")
    def test_create_http_manager(self, mock_pool_manager):
        network_manager = NetworkManager(
            proxy_url=None,
            random_agent=False,
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
        self.assertIsNotNone(network_manager.http_manager)

    @patch("okadminfinder.network.NetworkManager.request")
    def test_check_url(self, mock_request):
        network_manager = NetworkManager(
            proxy_url=None,
            random_agent=False,
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
        mock_request.return_value.status = 200
        self.assertTrue(network_manager.check_url("http://example.com"))


if __name__ == "__main__":
    unittest.main()
