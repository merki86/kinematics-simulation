import pygame

from properties import *
from ruler import Ruler
from object import Object
from panel import Panel

pygame.init()

# Rules:
# 1 meter = 10 px
#
#
#

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanics simulations - Kinematics")

clock = pygame.time.Clock()
ruler = Ruler(pygame.Color(255, 0, 0))
object = Object(1)
panel = Panel()

running = True

while running:
    # limit loop iteration per time
    # dt = delta time, time passed since last frame (ms)
    dt = clock.tick(FPS) / 1000

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        object.handle_event(event)
    
    # wipe
    screen.fill((0, 0, 0))

    # update logic
    object.update(dt)

    # render all the surfaces onto original Surface
    canvas_pos = pygame.Vector2(width_margin, height_margin)
    screen.blit(object.draw(), canvas_pos)
    screen.blit(ruler.draw(), canvas_pos)
    screen.blit(panel.draw(dt, object.mouse_pos, object.position, object.velocity, object.acceleration), (0, 0))

    # reveal on screen
    pygame.display.flip()

pygame.quit()