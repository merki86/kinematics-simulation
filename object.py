import pygame

from properties import *

class Object:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.position = pygame.Vector2(canvas_width/2, 0)
        self.mouse_pos = pygame.Vector2(0, 0)

        self.surface = pygame.Surface((canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), pygame.SRCALPHA)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_pos = pygame.Vector2(event.pos[0]-width_margin, event.pos[1]-height_margin) / pixels_in_meter
                self.position = self.mouse_pos

    def update(self, time) -> tuple[pygame.Vector2, pygame.Vector2]:
        dy = 0

        return self.mouse_pos, self.position

    def draw(self) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        pygame.draw.circle(self.surface, (255, 255, 0), (self.position.x*pixels_in_meter, self.position.y*pixels_in_meter), self.radius*pixels_in_meter)
        pygame.draw.circle(self.surface, (255, 0, 255), (self.position.x*pixels_in_meter, self.position.y*pixels_in_meter), pixels_in_meter//5)
        pygame.draw.circle(self.surface, (0, 255, 0), (self.mouse_pos.x*pixels_in_meter, self.mouse_pos.y*pixels_in_meter), pixels_in_meter//5)

        return self.surface