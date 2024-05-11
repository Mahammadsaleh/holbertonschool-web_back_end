#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple
index_range = __import__("0-simple_helper_function").index_range


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
        assert isinstance(page, int) and isinstance(page_size, int), "Page" + \
            " and page_size must be integers"
        assert page > 0 and page_size > 0, "Page and" + \
            "page_size must be positive"
        start, end = index_range(page, page_size)
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range - calculates a start index and an end index
    @page: number of page
    @page_size: size of page
    Return: tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
