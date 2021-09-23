import numpy as np


def p1(k: int) -> str:
    pass


def p2_a(x: list, y: list) -> list:
    pass


def p2_b(x: list, y: list) -> list:
    pass


def p2_c(x: list, y: list) -> list:
    pass


def p2_d(x: list, y: list) -> list:
    pass


def p3_a(x: set, y: set, z: set) -> set:
    pass


def p3_b(x: set, y: set, z: set) -> set:
    pass


def p3_c(x: set, y: set, z: set) -> set:
    pass


def p4_a() -> np.array:
    pass


def p4_b(x: np.array) -> list:
    pass


def p5_a(x: dict) -> int:
    pass


def p5_b(x: dict) -> int:
    pass


def p5_c(x: dict) -> list:
    pass


def p5_d(x: dict) -> np.array:
    pass


class PriorityQueue(object):
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


if __name__ == '__main__':
    print(p1(k=8))
    print('-----------------------------')
    print(p2_a(x=[], y=[1, 3, 5]))
    print(p2_b(x=[2, 4, 6], y=[]))
    print(p2_c(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print(p2_d(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print('------------------------------')
    print(p3_a(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_b(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_c(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print('------------------------------')
    print(p4_a())
    print(p4_b(p4_a()))
    print('------------------------------')
    graph = {
        'A': ['D', 'E'],
        'B': ['E', 'F'],
        'C': ['E'],
        'D': ['A', 'E'],
        'E': ['A', 'B', 'C', 'D'],
        'F': ['B'],
        'G': []
    }
    print(p5_a(graph))
    print(p5_b(graph))
    print(p5_c(graph))
    print(p5_d(graph))
    print('------------------------------')
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('kiwi')
    pq.push('orange')
    while not pq.is_empty():
        print(pq.pop())
