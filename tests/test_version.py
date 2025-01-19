import unittest

from okadminfinder import __creator__, __maintainer__, __version__


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "2.0.0")
        self.assertEqual(__creator__, "O.Koleda")
        self.assertEqual(__maintainer__, "mIcHyAmRaNe")


if __name__ == "__main__":
    unittest.main()
