import pygame
import game_constants as gc
import illustrator

from Node import Node
from Problem import Problem


def make_graph(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col


def main(search_agent_init):
    graph = make_graph(gc.ROWS, gc.WIDTH)
    illustrator.draw(gc.WIN, graph)

    start_state = None
    goal_state = None

    run = True

    while run:
        illustrator.draw(gc.WIN, graph)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, gc.ROWS, gc.WIDTH)
                node = graph[row][col]
                if not start_state and node != goal_state:
                    start_state = node
                    start_state.make_start()

                elif not goal_state and node != start_state:
                    goal_state = node
                    goal_state.make_end()

                elif node != goal_state and node != start_state:
                    node.make_barrier()

                illustrator.draw(gc.WIN, graph)
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, gc.ROWS, gc.WIDTH)
                node = graph[row][col]
                node.reset()

                if node == start_state:
                    start_state = None
                elif node == goal_state:
                    goal_state = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_state and goal_state:
                    for row in graph:
                        for node in row:
                            node.update_neighbors(graph)

                    problem = Problem(graph, start_state, goal_state)
                    search_agent = search_agent_init(graph, problem)
                    search_agent.algorithm()
                    search_agent.walk_path()

                if event.key == pygame.K_c:
                    start_state = None
                    goal_state = None
                    graph = make_graph(gc.ROWS, gc.WIDTH)

        # drawing.draw(win, graph, ROWS, width)
    pygame.quit()
