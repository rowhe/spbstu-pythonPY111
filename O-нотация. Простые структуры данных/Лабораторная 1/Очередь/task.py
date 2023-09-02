"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Описать где начало и конец очереди
        """
        self.queue = []  #  инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.insert(0, elem)  #  реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError

        return self.queue.pop()  #  реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        try:
            self.queue[ind]
        except IndexError:
            return None

        inv = -ind - 1
        return self.queue[inv]  #  реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue.clear()  #  реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue)  #  реализовать метод __len__
