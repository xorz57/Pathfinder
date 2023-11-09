import pygame

from screens.pathfinder import Pathfinder

pygame.init()
screen = pygame.display.set_mode((16 * 32, 16 * 32))

clock = pygame.time.Clock()
running = True

current_screen = Pathfinder()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_screen.handle_events(event)

    screen.fill("black")

    current_screen.update()
    current_screen.render(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
