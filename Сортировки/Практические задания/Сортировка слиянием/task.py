from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # реализуйте сортировку слиянием


    if len(container) < 2:
        return container

    middle = len(container) // 2
    left_part = sort(container[:middle])
    right_part = sort(container[middle:])
    def _merge(lefty, righty):

        merged_container = []

        while True:
            if not lefty:
                merged_container += righty
                break
            if not righty:
                merged_container += lefty
                break
            if lefty[0] <= righty[0]:
                elem = lefty.pop(0)
                merged_container.append(elem)
            else:
                elem = righty.pop(0)
                merged_container.append(elem)
        return merged_container

    return _merge(left_part, right_part)
