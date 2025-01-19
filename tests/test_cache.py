import unittest

from okadminfinder import (
    disable_cache,
    invalidate_all_cache,
    is_cache_enabled,
    memoize_if_cache_enabled,
)


class TestCache(unittest.TestCase):
    def test_invalidate_all_cache(self):
        invalidate_all_cache()
        self.assertTrue(True)  # Just to ensure the function runs without errors

    def test_disable_cache(self):
        disable_cache()
        self.assertFalse(is_cache_enabled())

    def test_memoize_if_cache_enabled(self):
        @memoize_if_cache_enabled
        def dummy_function(x):
            return x * 2

        self.assertEqual(dummy_function(5), 10)


if __name__ == "__main__":
    unittest.main()
