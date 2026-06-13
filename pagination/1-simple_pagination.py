#!/usr/bin/env python3
import csv
import math
from typing import List
""" Simple pagination page getting"""


def index_range(page, page_size):
    """Returns a tuple for pagination helper function """

    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """page getter function"""
        assert isinstance(page, int), "Page must be an integer"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page > 0, "Page must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"
        pages = []
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        pages = dataset[start:end]
        return pages
