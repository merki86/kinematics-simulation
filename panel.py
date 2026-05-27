import pygame

from properties import *

class Panel:
    def __init__(self) -> None:
        self.surface = pygame.Surface((canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), pygame.SRCALPHA)

        self.font_name = "sans-serif"
        self.font_size = 24

    def draw(self, time, dy) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        font = pygame.font.SysFont(self.font_name, self.font_size)

        self.surface.blit(font.render(f"time: {round(time, 3)}", True, (255, 255, 255)), (0, 0))
        self.surface.blit(font.render(f"displacement: {round(dy, 3)}", True, (255, 255, 255)), (0, 1*font.get_height()))

        return self.surface