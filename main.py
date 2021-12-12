# The entrance into the program
import path_finder
import pygame
import sys
import SearchAgents
import illustrator
from pygame.locals import *


def main():
    search_agent_init = get_search_agent_initializer()
    path_finder.main(search_agent_init)


def get_search_agent_initializer():
    illustrator.draw_main_screen()
    run = True
    search_agent_init = None

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_b:
                    search_agent_init = SearchAgents.BreadthFirstSearch

                if event.key == pygame.K_d:
                    search_agent_init = SearchAgents.DepthFirstSearch

                run = False

        pygame.display.update()

    return search_agent_init


if __name__ == "__main__":
    main()
