import pygame

from properties import *

class Object:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.position = pygame.Vector2(canvas_width/2, 0)

        self.surface = pygame.Surface((canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), pygame.SRCALPHA)

    def draw(self, time) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        pygame.draw.circle(self.surface, (255, 255, 0), (self.position.x*pixels_in_meter, self.position.y*pixels_in_meter), self.radius*pixels_in_meter)
        pygame.draw.circle(self.surface, (255, 0, 255), (self.position.x*pixels_in_meter, self.position.y*pixels_in_meter), pixels_in_meter//5)

        dy = 0**2 + 0.5*9.8*time**2 # y = ut + (1/2)gt2 , in meters
        if self.position.y + dy + self.radius >= canvas_height:
            self.position.y = canvas_height - self.radius
            dy = 0
        self.position.y += dy

        return self.surface