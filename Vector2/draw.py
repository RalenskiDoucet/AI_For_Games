#pylint: disable=E1101

import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080))
    screen.fill((0, 0, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()


main()