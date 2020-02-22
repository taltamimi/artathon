import pygame
import random
import math

pygame.init()
size = width, height = (1920, 1080)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
blue = (0, 0, 255)
sand = (245, 222, 173)
grey = (200, 200, 200)
black = (0, 0, 0)

boss_x = 50
boss_y = 350

boss_orbit = 0
ship_orbit = 0
i = 1

running = True

stars = [(random.randint(0, 1920), random.randint(0, 1080)) for x in range(140)]

index = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    boss_x = math.cos(boss_orbit) * 300 + width / 2
    boss_y = -math.sin(boss_orbit) * 100 + (height - 400) / 2

    ship_x = math.cos(ship_orbit) * 300 + boss_x
    ship_y = -math.sin(ship_orbit) * 300 + boss_y

    boss_orbit += .1
    ship_orbit += .03

    # reset the screen
    screen.fill(black)
    pygame.draw.rect(screen, blue, pygame.Rect((0, 1900), size), width)

    # draw the stars
    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))
    i = i * -1

    print(boss_orbit)
    island = pygame.image.load("island.png")

    moon = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Unknown (1).png").convert(), (160, 200)),
                                   i * 5)
    ship = pygame.transform.scale((pygame.image.load("ship.png")), (300, 200))
    boss = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Picture1.png"), (160, 200)), boss_orbit < 3,
                                 False)

    sea = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("sea.png"), (width, 300)), i * 0.05)

    # pygame.draw.circle(screen, sand, island_place, island)
    screen.blit(sea, (0, height - 200))

    screen.blit(island, (int(width / 2) - 200, height - 550))

    screen.blit(boss, (int(boss_x), int(boss_y)))
    screen.blit(ship, (int(ship_x), int(ship_y)))
    screen.blit(moon, (int(100), int(100)))

    # pygame.draw.circle(screen, grey, (int(ship_x), int(ship_y)), 5)

    pygame.display.flip()

    index += 1
    pygame.image.save(screen, "dr2/Image%06d.png" % index)
    if index > 40000:
        break

pygame.quit()