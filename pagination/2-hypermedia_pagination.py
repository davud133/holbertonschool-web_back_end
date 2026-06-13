#!/usr/bin/env python3
"""Simple module for paginating a dataset."""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculates the start and end index for a given page.
    Args:
        page: The current page number.
        page_size: The number of items on each page.
    Returns:
        A tuple of (start_index, end_index).
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Handles loading and paginating the popular baby names database."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Sets up an empty cache for the dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.
        Returns:
            The dataset rows as a list of lists (excluding the header).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data.
        Args:
            page: The page number to get (must be > 0).
            page_size: The number of records per page (must be > 0).
        Returns:
            A list of rows representing the requested page.
        """
        assert isinstance(page, int), "Page must be an integer"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page > 0, "Page must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"
        pages = []
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        pages = dataset[start:end]
        return pages
    def get_hyper(page = 1, page_size = 1):
        """getting hyper function"""

        dataset = self.dataset()
        total_pages = len(dataset) / page_size
        next = None
        prev = None
        if page < total_pages:
            next = page + 1
        if page > 1:
            prev = page - 1
        datas = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next,
            "perv_page": prev
            "total_pages": total_pages
            }
        return datas
