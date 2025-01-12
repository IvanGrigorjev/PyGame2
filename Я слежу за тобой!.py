import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Я слежу за тобой!')
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    screen.fill('black')

    k = 0
    color_font = pygame.Color('red')

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWEXPOSED:
                k += 1

        font = pygame.font.Font(None, 100)
        text = font.render(str(k), 1, (255, 0, 0))
        screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
        pygame.display.flip()
        screen.fill('black')
    pygame.quit()
