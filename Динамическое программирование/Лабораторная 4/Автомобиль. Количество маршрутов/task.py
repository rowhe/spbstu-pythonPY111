from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # решить задачу с помощью динамического программирования

    fields = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            fields[i][j] = fields[i][j-1]+fields[i-1][j]+fields[i-1][j-1]
    return fields


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
