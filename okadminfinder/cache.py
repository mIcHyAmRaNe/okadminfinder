#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from functools import wraps

import diskcache as dc

# Initialize the cache
if os.name == "nt":  # Windows
    temp_dir = os.getenv("TEMP")
else:  # Unix-like systems
    temp_dir = "/tmp"

# Create the cache in the appropriate temporary directory
cache = dc.Cache(os.path.join(temp_dir, "okadminfinder_cache"))
cache_enabled = True  # Default state: cache is enabled


def invalidate_all_cache():
    """
    Invalidate all cache entries
    """
    cache.clear()


def disable_cache():
    """
    Disable the cache
    """
    global cache_enabled
    cache_enabled = False


def is_cache_enabled() -> bool:
    """
    Check if cache is enabled
    """
    return cache_enabled


def memoize_if_cache_enabled(func):
    """
    Memoization decorator that respects the cache enabled state
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_cache_enabled():
            # Exclude the 'self' object from the cache key
            cache_key = (func.__name__, args[1:], kwargs)
            if cache_key in cache:
                return cache[cache_key]
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
        else:
            return func(*args, **kwargs)

    return wrapper
