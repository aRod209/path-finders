import pygame

import color_constants as color

def draw(win, graph, rows, width):
    win.fill(color.GREY)

    for row in graph:
        for node in row:
            node.draw(win)

    pygame.display.update()