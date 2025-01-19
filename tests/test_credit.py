import unittest

from okadminfinder.credit import Credit


class TestCredit(unittest.TestCase):
    def test_set_credit(self):
        credit = Credit()
        with credit.set_credit():
            self.assertTrue(
                True
            )  # Just to ensure the context manager runs without errors


if __name__ == "__main__":
    unittest.main()
