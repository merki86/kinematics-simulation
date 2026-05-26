import pygame
from ruler import Ruler

pygame.init()

# Rules:
# 1 meter = 10 px
#
#
#

FPS = 60
WIDTH = 500
HEIGHT = 500
pixels_in_meter = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanics simulations - Kinematics")

clock = pygame.time.Clock()
ruler = Ruler()

time = 0
canvas_width = WIDTH / pixels_in_meter
canvas_height = HEIGHT / pixels_in_meter
object_radius = 1
object_pos = pygame.Vector2(canvas_width/2, 0)

running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # wipe
    screen.fill((0, 0, 0))

    # draw the Ruler Surface onto original Surface    
    screen.blit(ruler.draw(), (0, 0))

    # render
    pygame.draw.circle(screen, (255, 255, 0), (object_pos.x*pixels_in_meter, object_pos.y*pixels_in_meter), object_radius*pixels_in_meter)

    dy = 0**2 + 0.5*9.8*time**2 # y = ut + (1/2)gt2 , in meters
    if object_pos.y + dy + object_radius >= canvas_height:
        object_pos.y = canvas_height - object_radius
        dy = 0
    object_pos.y += dy

    # reveal on screen
    pygame.display.flip()

    # limit loop iteration per time
    # dt = delta time, time passed since last frame (ms)
    dt = clock.tick(FPS)
    time += dt / 1000

pygame.quit()