from random import randint

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Перетаскивание')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    screen.fill('black')

    color_rect = pygame.Color('green')
    a = 100
    rect_x, rect_y = 0, 0
    d_x, d_y = 0, 0

    move = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rect_x <= event.pos[0] <= rect_x + a and rect_y <= event.pos[1] <= rect_y + a:
                    move = True
            if event.type == pygame.MOUSEMOTION:
                if move:
                    d_x, d_y = event.rel
                    rect_x, rect_y = rect_x + d_x, rect_y + d_y
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                move = False

        pygame.draw.rect(screen, color_rect, (rect_x, rect_y, a, a), 0)

        pygame.display.flip()
        screen.fill('black')
    pygame.quit()
