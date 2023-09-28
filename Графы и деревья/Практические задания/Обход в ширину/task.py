from typing import Hashable, List
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt



def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    #  реализовать обход в ширину

    path = []
    visited = {node: False for node in g.nodes}
    d = []
    d.append(start_node)
    visited[start_node] = True

    while d:
        current_node = d.pop(0)
        path.append(current_node)
        for neighbour in g[current_node]:
            if not visited[neighbour]:
                d.append(neighbour)
                visited[neighbour] = True

    return path


if __name__ == '__main__':
    #  записать граф с помощью модуля networkx и прверить обход в ширину
    g = nx.Graph()
    g.add_nodes_from("ABCDEFGHIJK")
    g.add_edges_from([

        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'J'),
        ('H', 'E'),
        ('H', 'D'),
        ('E', 'D')

    ])

    nx.draw(g, with_labels=True)
    plt.show()
    print(bfs(g, "A"))

