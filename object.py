import pygame

from properties import *

class Object:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.position = pygame.Vector2(canvas_width/2, 0)
        self.initial_velocity = pygame.Vector2(0, 0)
        self.velocity = self.initial_velocity.copy()
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1

        self.mouse_pos = pygame.Vector2(0, 0)

        self.surface = pygame.Surface((canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), pygame.SRCALPHA)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_pos = pygame.Vector2(abs(event.pos[0]-width_margin) / pixels_in_meter, abs(canvas_height-(event.pos[1]-height_margin) / pixels_in_meter))
                self.position = self.mouse_pos.copy()

    def update(self, dt) -> None:
        # computing forces
        gravity_force = self.mass * 9.8 * 0

        # computing net force
        net_force = pygame.Vector2(0, 0-gravity_force)

        # computing acceleration
        self.acceleration = net_force / self.mass

        # computing velocity
        self.velocity += self.acceleration*dt

        # computing position
        self.position += self.velocity*dt

        if self.position.y + self.radius >= canvas_height:
            self.position.y = canvas_height - self.radius
            self.velocity = -self.velocity

    def draw(self) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        pygame.draw.circle(self.surface, (255, 255, 0), (self.position.x*pixels_in_meter, (canvas_height-self.position.y)*pixels_in_meter), self.radius*pixels_in_meter)
        pygame.draw.circle(self.surface, (255, 0, 255), (self.position.x*pixels_in_meter, (canvas_height-self.position.y)*pixels_in_meter), pixels_in_meter//5)
        pygame.draw.circle(self.surface, (0, 255, 0), (self.mouse_pos.x*pixels_in_meter, (canvas_height-self.position.y)*pixels_in_meter), pixels_in_meter//5)

        return self.surface