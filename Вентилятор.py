import math

import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Вентилятор')
    screen.fill('black')

    clock = pygame.time.Clock()
    fps = 30
    rotetion_angle = 0
    speed = 0
    r = 10
    a = 70
    angle = math.radians(30)
    osnovanie = math.sqrt(2 * (a ** 2) - (2 * a ** 2 * math.cos(angle)))
    coords = [
    [(101, 101), (101 + osnovanie / 2, 101 - a), (101 - osnovanie / 2, 101 - a)],
    [(101, 101), (171, 121), ((101 + osnovanie / 2) + 35, 150)],
    [(101, 101), (101 - 70, 121), ((101 - osnovanie / 2) - 35, 150)]
]

color = pygame.Color('white')

screen2 = pygame.Surface((201, 201), pygame.SRCALPHA)
pygame.draw.circle(screen2, color, (101, 101), center_radius)
pygame.draw.polygon(screen2, color, coords[0])
pygame.draw.polygon(screen2, color, coords[1])
pygame.draw.polygon(screen2, color, coords[2])

    running = True
while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rotation_speed -= 1
            elif event.button == 3:
                rotation_speed += 1

        if event.type == pygame.MOUSEBUTTONUP:
            pass

    transform_angle += rotation_speed

    rotated_surface = pygame.transform.rotate(screen2, transform_angle)
    rect = rotated_surface.get_rect(center=(101, 101))
    screen.blit(rotated_surface, rect)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()