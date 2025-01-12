import pygame

pygame.init()
size = width, height = 300, 200
screen = pygame.display.set_mode(size)
screen.fill("white")

color = pygame.Color("red")
brick = (30, 15)
shift = 15
clearance = 2

for i in range(0, size[1], brick[1] + clearance):
    for j in range(0, size[0], brick[0] + clearance):
        if i % 2 != 0:
            j -= shift
        pygame.draw.rect(screen, color, (j, i, brick[0], brick[1]))

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
