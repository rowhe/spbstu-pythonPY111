from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    #  реализовать алгоритм быстрой сортировки
    if not container:
        return container

    start = container[0]

    left_part = [elem for elem in container if elem < start]
    right_part = [elem for elem in container if elem > start]
    middle_part = [elem for elem in container if elem == start]

    return (sort(left_part) + middle_part + sort(right_part))
