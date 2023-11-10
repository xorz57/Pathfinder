import pygame

from config import WINDOW_W, WINDOW_H, WINDOW_TITLE
from screens.pathfinder_screen import PathfinderScreen

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption(WINDOW_TITLE)

clock = pygame.time.Clock()
running = True

current_screen = PathfinderScreen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_screen.handle_events(event)

    screen.fill("black")

    current_screen.update()
    current_screen.render(screen)

    pygame.display.flip()

    clock.tick(240)

pygame.quit()
