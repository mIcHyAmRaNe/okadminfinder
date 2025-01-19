import unittest
from unittest.mock import patch

from okadminfinder.app import main, run


class TestApp(unittest.TestCase):
    @patch("okadminfinder.app.app")
    def test_run(self, mock_app):
        run()
        mock_app.assert_called_once()

    @patch("okadminfinder.app.Process")
    @patch("okadminfinder.app.Typer")
    def test_main(self, mock_typer, mock_process):
        # Mock the Typer options to avoid actual command-line parsing
        mock_typer.return_value.parse_args.return_value = {
            "url": "http://example.com",
            "random_agent": False,
            "proxy": None,
            "tor": False,
            "wordlist": None,
            "dns": False,
            "fuzz": False,
            "output": None,
            "clear_cache": False,
            "timeout": 10,
            "num_pools": 50,
            "threads": 16,
            "retry": 0,
            "debug": False,
        }
        main()
        mock_process.assert_called_once()


if __name__ == "__main__":
    unittest.main()
