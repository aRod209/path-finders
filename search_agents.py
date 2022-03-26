from operator import ne
import sys
import pygame
from pygame.locals import *
import time
import color_constants as color
import illustrator
import game_constants as gc
from queue import PriorityQueue
from fringe import Stack
from fringe import Queue


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

    def manhattan_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)


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
                    if neighbor in closed:
                        continue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor is not start_node:
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
                    if neighbor in closed:
                        continue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    fringe.add((neighbor, new_path))

                    if neighbor is not start_node:
                        neighbor.make_open()
                    illustrator.draw(gc.WIN, self.graph)
                if node != start_node:
                    node.make_closed()

            illustrator.draw(gc.WIN, self.graph)

class IterativeDeepiningDepthFirstSearch(SearchAgent):

    def algorithm(self):
        for depth in range(50):
            print(f'Current depth at: {depth}')
            self.depth_limited_search(depth)

            if self.problem.path:
                return

            illustrator.reset_closed_nodes(gc.WIN, self.graph, self.problem.goal_state)
            

    def depth_limited_search(self, max_depth):
        fringe = Stack()
        start_node = self.problem.start_state
        goal_node = self.problem.goal_state

        fringe.add([start_node, [start_node], 0])

        while not fringe.is_empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            node, path, current_depth = fringe.pop()

            if node == goal_node:
                path.append(node)
                self.problem.path = path
                return

            if current_depth >= max_depth:
                continue

            for neighbor in node.neighbors:

                new_path = path.copy()
                new_path.append(neighbor)
                fringe.add([neighbor, new_path, current_depth + 1])

                if neighbor is not start_node:
                    neighbor.make_open()
                illustrator.draw(gc.WIN, self.graph)
            if node != start_node:
                node.make_closed()

            illustrator.draw(gc.WIN, self.graph)

    def depth_from_start_state(self, node):
        x1,y1 = node.get_pos()
        x2,y2 = self.problem.start_state.get_pos()
        return self.manhattan_distance(x1, y1, x2, y2)

class UniformCostSearch(SearchAgent):

    def algorithm(self):
        closed = set()
        fringe = PriorityQueue()
        start_node = self.problem.start_state
        goal_node = self.problem.goal_state

        g_cost = 0
        tie_breaker = 0
        fringe.put((g_cost, tie_breaker, (start_node, [start_node])))

        while fringe:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            g_cost, tie_breaker, node_and_path = fringe.get()
            node, path = node_and_path

            if node == goal_node:
                path.append(node)
                self.problem.path = path
                return

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    if neighbor in closed:
                        continue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    new_g_cost = g_cost + neighbor.cost
                    tie_breaker += 1
                    fringe.put((new_g_cost, tie_breaker, (neighbor, new_path)))

                    if neighbor is not start_node:
                        neighbor.make_open()
                    illustrator.draw(gc.WIN, self.graph)

                if node != start_node:
                    node.make_closed()

            illustrator.draw(gc.WIN, self.graph)

class AStarSearch(SearchAgent):

    def algorithm(self):
        closed = set()
        fringe = PriorityQueue()
        start_node = self.problem.start_state
        goal_node = self.problem.goal_state

        f_cost = 0
        g_cost = 0
        tie_breaker = 0
        fringe.put((f_cost, tie_breaker, g_cost, (start_node, [start_node])))

        while fringe:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            f_cost, tie_breaker, g_cost, node_and_path = fringe.get()
            node, path = node_and_path

            if node == goal_node:
                path.append(node)
                self.problem.path = path
                return

            if node not in closed:
                closed.add(node)

                for neighbor in node.neighbors:
                    if neighbor in closed:
                        continue
                    new_path = path.copy()
                    new_path.append(neighbor)
                    new_g_cost = g_cost + neighbor.cost
                    new_f_cost = new_g_cost + self.hueristic(neighbor)
                    tie_breaker += 1
                    fringe.put((new_f_cost, tie_breaker, new_g_cost, (neighbor, new_path)))

                    if neighbor is not start_node:
                        neighbor.make_open()
                    illustrator.draw(gc.WIN, self.graph)

                if node != start_node:
                    node.make_closed()

            illustrator.draw(gc.WIN, self.graph)

    def hueristic(self, node):
        x1,y1 = node.get_pos()
        x2,y2 = self.problem.goal_state.get_pos()
        return self.manhattan_distance(x1, y1, x2, y2)