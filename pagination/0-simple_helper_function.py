#!/usr/bin/env python3
"""Returns a tuple for pagination helper function"""


def index_range(page, page_size):
    """Returns a tuple for pagination helper function """

    return ((page - 1) * page_size, page * page_size)
