import color_constants as color
import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = color.LIGHT_GREEN
        self.cost = 1
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == color.PURPLE

    def is_open(self):
        return self.color == color.RED

    def is_barrier(self):
        return self.color == color.BLACK

    def is_start(self):
        return self.color == color.BLUE

    def is_end(self):
        return self.color == color.GOLD

    def is_low_cost(self):
        return self.color == color.LIGHT_GREEN

    def is_medium_cost(self):
        return self.color == color.GREEN

    def is_high_cost(self):
        return self.color == color.DARK_GREEN

    def reset(self):
        self.color = color.LIGHT_GREEN

    def make_start(self):
        self.color = color.BLUE

    def make_closed(self):
        self.color = color.PURPLE

    def make_open(self):
        self.color = color.RED

    def make_barrier(self):
        self.color = color.BLACK

    def make_end(self):
        self.color = color.GOLD

    def make_medium_cost(self):
        if not self.is_start() and not self.is_end():
            self.cost = 5
            self.color = color.GREEN

    def make_high_cost(self):
        if not self.is_start() and not self.is_end():
            self.cost = 10
            self.color = color.DARK_GREEN

    def make_path(self):
        self.color = color.WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width-1, self.width-1))

    def update_neighbors(self, graph):
        self.neighbors = []

        if self.row > 0 and not graph[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(graph[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not graph[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(graph[self.row][self.col + 1])

        if self.col > 0 and not graph[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(graph[self.row][self.col - 1])

        if self.row < self.total_rows - 1 and not graph[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(graph[self.row + 1][self.col])

    def __lt__(self, other_node):
        return self.cost < other_node.cost
        
