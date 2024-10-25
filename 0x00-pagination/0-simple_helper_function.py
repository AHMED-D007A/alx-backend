#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page, page_size):
    """Return a tuple of size two containing a start index and an end index"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)
    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
