import pygame
import color_constants as color
import game_constants as gc


def draw_main_screen():
    pygame.init()
    pygame.display.set_mode((gc.WIDTH, gc.HEIGHT))
    pygame.display.set_caption('Path Finders Visualizer')
    my_font = pygame.font.SysFont('arial', 30)
    title_text = my_font.render('Path Finders Visualizer', False, color.BLACK)
    bfs_text = my_font.render('Press b for Breadth First Search', False, color.RED)
    dfs_text = my_font.render('Press d for Depth First Search', False, color.RED)
    gc.WIN.fill(color.WHITE)
    gc.WIN.blit(title_text, (250, 0))
    gc.WIN.blit(bfs_text, (200, 200))
    gc.WIN.blit(dfs_text, (200, 250))


def draw(win, graph):
    win.fill(color.GREY)

    for row in graph:
        for node in row:
            node.draw(win)

    pygame.display.update()
