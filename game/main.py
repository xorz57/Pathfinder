import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from screens.pathfinder import Pathfinder

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

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

    clock.tick(240)

pygame.quit()
