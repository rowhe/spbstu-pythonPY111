"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # реализовать итеративный линейный поиск
    if not arr:
        raise ValueError

    min_ind = 0
    min_elem = arr[min_ind]

    for ind in range(len(arr)):
        if arr[ind] < min_elem:
            min_elem = arr[ind]
            min_ind = ind
    return min_ind



