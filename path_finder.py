import pygame
import time
import color_constants as color
import game_constants
import drawing

from Node import Node
from Problem import Problem
from SearchAgent import SearchAgent

pygame.display.set_caption("Search Algorithms Visualizer")


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


def main(win, width):
    ROWS = 40
    graph = make_graph(ROWS, width)
    drawing.draw(win, graph, ROWS, width)

    start_state = None
    goal_state = None

    run = True
    while run:
        drawing.draw(win, graph, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = graph[row][col]
                if not start_state and node != goal_state:
                    start_state = node
                    start_state.make_start()

                elif not goal_state and node != start_state:
                    goal_state = node
                    goal_state.make_end()

                elif node != goal_state and node != start_state:
                    node.make_barrier()

                drawing.draw(win, graph, ROWS, width)
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
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
                    search_agent = SearchAgent(graph, problem)
                    path = search_agent.dfs()

                    for node in path:
                        if node is start_state:
                            continue
                        node.make_path()
                        drawing.draw(win, graph, ROWS, width)

                    curr = start_state

                    for node in path[1:]:
                        curr.color = color.WHITE
                        node.color = color.BLUE
                        curr = node
                        time.sleep(0.2)
                        drawing.draw(win, graph, ROWS, width)

                if event.key == pygame.K_c:
                    start_state = None
                    goal_state = None
                    graph = make_graph(ROWS, width)

        # drawing.draw(win, graph, ROWS, width)
    pygame.quit()


if __name__ == "__main__":
    main(game_constants.WIN, game_constants.WIDTH)
