import pygame

from properties import *
from ruler import Ruler
from object import Object

pygame.init()

# Rules:
# 1 meter = 10 px
#
#
#

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanics simulations - Kinematics")

clock = pygame.time.Clock()
ruler = Ruler(5, pygame.Color(255, 0, 0))
object = Object(5)

time = 0
running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # wipe
    screen.fill((0, 0, 0))

    # render all the surfaces onto original Surface
    screen.blit(ruler.draw(), (0, 0))
    screen.blit(object.draw(time), (0, 0))

    # reveal on screen
    pygame.display.flip()

    # limit loop iteration per time
    # dt = delta time, time passed since last frame (ms)
    dt = clock.tick(FPS)
    time += dt / 1000

pygame.quit()