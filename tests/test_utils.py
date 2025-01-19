import unittest

from okadminfinder._utils import URLCreator, UserAgent


class TestUtils(unittest.TestCase):
    def test_user_agent(self):
        user_agent = UserAgent()
        self.assertIsNotNone(user_agent.get_user_agent())

    def test_url_creator(self):
        url_creator = URLCreator(wordlist=None, dns=False, fuzz=False)
        self.assertIsNotNone(url_creator.create_urls("http://example.com"))


if __name__ == "__main__":
    unittest.main()
