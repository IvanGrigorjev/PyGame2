import pygame

WINDOW_SIZE = WINDOW_width, WINDOW_height = 800, 600
FPS = 60


class Balloon:
    def __init__(self, x, y):
        self.r = 10
        self.v_x = 100
        self.v_y = 100
        self.ball_color = pygame.Color('white')
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()

    def render(self, screen):
        pygame.draw.circle(screen, self.ball_color, (self.x, self.y), self.r)

        self.x -= self.v_x / FPS
        self.y -= self.v_y / FPS
        if self.y < self.r or self.y > WINDOW_height - self.r:
            self.v_y = -self.v_y
        if self.x < self.r or self.x > WINDOW_width - self.r:
            self.v_x = -self.v_x

        self.clock.tick(FPS)


def main():
    pygame.init()
    pygame.display.set_caption('Шарики')

    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill('black')
    balls = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                balls.append(Balloon(x, y))
        screen.fill('black')
        for ball in balls:
            ball.render(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
