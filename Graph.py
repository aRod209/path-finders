import game_constants as gc
from Node import Node

class Graph:
    def __init__(self):
        self.matrix = []
        self.cost_matrix = [[0] * gc.ROWS] * gc.ROWS

        for i in range(gc.ROWS):
            self.matrix.append([])
            for j in range(gc.ROWS):
                node = Node(i, j, gc.WIDTH//gc.ROWS, gc.ROWS)
                self.matrix[i].append(node)