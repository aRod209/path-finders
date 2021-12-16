import pygame
import game_constants as gc
import illustrator
from graph import Graph
from problem import Problem


def main(search_agent_init):
    graph = Graph()
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
                row, col = graph.get_clicked_pos(pos)
                node = graph.matrix[row][col]

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
                row, col = graph.get_clicked_pos(pos)
                node = graph.matrix[row][col]
                node.reset()

                if node == start_state:
                    start_state = None
                elif node == goal_state:
                    goal_state = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_state and goal_state:
                    for row in graph.matrix:
                        for node in row:
                            node.update_neighbors(graph.matrix)

                    problem = Problem(graph.matrix, start_state, goal_state)
                    search_agent = search_agent_init(graph, problem)
                    search_agent.algorithm()
                    search_agent.walk_path()

                if event.key == pygame.K_c:
                    start_state = None
                    goal_state = None
                    graph = Graph()

            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_LSHIFT]:
                pos = pygame.mouse.get_pos()
                row, col = graph.get_clicked_pos(pos)
                node = graph.matrix[row][col]
                node.make_medium_cost()

            if keys[pygame.K_LALT]:
                pos = pygame.mouse.get_pos()
                row, col = graph.get_clicked_pos(pos)
                node = graph.matrix[row][col]
                node.make_high_cost()

    pygame.quit()
