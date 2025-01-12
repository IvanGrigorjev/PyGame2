import pygame

size = width, height = 501, 501
screen = pygame.display.set_mode(size)
screen.fill('black')

x, y = 251, 251
x_new, y_new = x, y
color_ball = pygame.Color('red')
fps = 60
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_new, y_new = event.pos
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    pygame.draw.circle(screen, color_ball, (x, y), 20)

    if x_new > x:
        x += 1
    elif x_new < x:
        x -= 1
    if y_new > y:
        y += 1
    elif y_new < y:
        y -= 1

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()