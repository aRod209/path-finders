import time
import pygame
import game_constants

from Stack import Stack
from Queue import Queue
import drawing
import game_constants


class SearchAgent:
    def __init__(self, graph, problem):
        self.graph = graph
        self.problem = problem

    def dfs(self):
        closed = set()
        fringe = Stack()
        start_node = self.problem.start_state
        goal_node = self.problem.goal_state

        fringe.add((start_node, [start_node]))

        while not fringe.is_empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            node, path = fringe.pop()
            
            if node == goal_node:
                path.append(node)
                return path

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor not in closed and neighbor is not start_node:
                        neighbor.make_open()
                    drawing.draw(game_constants.WIN, self.graph, 50, game_constants.WIDTH)
                if node != start_node:
                    node.make_closed()

            drawing.draw(game_constants.WIN, self.graph, 50, game_constants.WIDTH)

    def bfs(self):
        closed = set()
        fringe = Queue()
        start_node = self.problem.start_state
        goal_node = self.problem.goal_state

        fringe.add((start_node, [start_node]))

        while not fringe.is_empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            node, path = fringe.pop()
            
            if node == goal_node:
                path.append(node)
                return path

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor not in closed and neighbor is not start_node:
                        neighbor.make_open()
                    drawing.draw(game_constants.WIN, self.graph, 50, game_constants.WIDTH)
                if node != start_node:
                    node.make_closed()

            drawing.draw(game_constants.WIN, self.graph, 50, game_constants.WIDTH)