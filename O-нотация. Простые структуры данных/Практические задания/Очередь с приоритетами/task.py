"""
Priority Queue
Queue priorities are from 0 to 10
"""
from typing import Any

from collections import deque


class PriorityQueue:
    HIGH_PRIORITY = 0  # наивысший приоритет
    LOW_PRIORITY = 10  # наименьший приоритет

    def __init__(self):
        self.p_q: dict[int, deque] = {priority: deque() for priority in range(self.HIGH_PRIORITY, self.LOW_PRIORITY + 1)}  # использовать deque для реализации очереди с приоритетами
        # print(self.p_q)

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Добавление элемент в конец очереди c учетом приоритета

        :param elem: Элемент, который должен быть добавлен
        :param priority: Приоритет добавляемого элемента
        """
        self.p_q[priority].append(elem)  # реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        for queue in self.p_q.values():
            if queue:
                return queue.popleft()
        raise IndexError("No queue")
          # реализовать метод dequeue

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди с указанным приоритетом, и т.д.)
        :param priority: Приоритет очереди

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        p_queue = self.p_q[priority]
        ...  # реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError
        if not 0 <= ind < len(p_queue):
            raise IndexError

        return p_queue[ind]


    def clear(self) -> None:
        """ Очистка очереди. """

        # реализовать метод clear
        for q in self.p_q.values():
            q.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
    # реализовать метод __len__
        len_ = 0
        for q in self.p_q.values():
            len_ = len(q)
        return len_


a = PriorityQueue()
