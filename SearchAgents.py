import sys
import pygame
from pygame.locals import *
import time
import color_constants as color
import illustrator
import game_constants as gc
from Stack import Stack
from Queue import Queue


class SearchAgent:
    def __init__(self, graph, problem):
        self.graph = graph
        self.problem = problem

    def walk_path(self):
        for node in self.problem.path:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if node is self.problem.start_state:
                continue
            node.make_path()
            illustrator.draw(gc.WIN, self.graph)

        curr = self.problem.start_state

        for node in self.problem.path[1:]:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if self.problem.goal_state.color == color.WHITE:
                self.problem.goal_state.color = color.GOLD
            else:
                self.problem.goal_state.color = color.WHITE
            curr.color = color.WHITE
            node.color = color.BLUE
            curr = node
            time.sleep(0.2)
            illustrator.draw(gc.WIN, self.graph)


class DepthFirstSearch(SearchAgent):

    def algorithm(self):
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
                self.problem.path = path
                return

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor not in closed and neighbor is not start_node:
                        neighbor.make_open()
                    illustrator.draw(gc.WIN, self.graph)
                if node != start_node:
                    node.make_closed()

            illustrator.draw(gc.WIN, self.graph)


class BreadthFirstSearch(SearchAgent):

    def algorithm(self):
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
                self.problem.path = path
                return

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor not in closed and neighbor is not start_node:
                        neighbor.make_open()
                    illustrator.draw(gc.WIN, self.graph)
                if node != start_node:
                    node.make_closed()

            illustrator.draw(gc.WIN, self.graph)
