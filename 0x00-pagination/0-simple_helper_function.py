#!/usr/bin/python3
"""
0. Simple helper function
"""


def index_range(page, page_size):
    """Return a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)