from random import randint

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = randint(200, 1024), randint(200, 768)
    screen = pygame.display.set_mode(size)
    screen.fill('blue')

    running = True
    x_pos = 0
    y_pos = 0
    color_circle = pygame.Color('yellow')
    r = 0
    v = 10
    fps = 30
    clock = pygame.time.Clock()
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill('blue')
                x_pos, y_pos = event.pos
                if drawing:
                    r = 0
                else:
                    drawing = True
        if drawing:
            pygame.draw.circle(screen, color_circle, (x_pos, y_pos), r)
            r += v / fps
            clock.tick(fps)

        pygame.display.flip()
    pygame.quit()