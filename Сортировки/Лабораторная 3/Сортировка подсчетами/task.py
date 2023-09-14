from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализовать алгоритм сортировки подсчетами


    if len(container) < 1:
        return container

    max_value = max(container)
    dop_list = [0] * (max_value + 1)

    for i in container:
        dop_list[i] += 1

    sorted_list = []

    for index, a in enumerate(dop_list):
        sorted_list.extend([index]*a)

    return sorted_list


