import pygame

from properties import *

class Panel:
    def __init__(self) -> None:
        self.surface = pygame.Surface((canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), pygame.SRCALPHA)

        self.font_name = "sans-serif"
        self.font_size = 24

    def draw(self, time, mouse_pos, obj_pos, obj_vel, obj_acc) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        font = pygame.font.SysFont(self.font_name, self.font_size)

        self.surface.blit(font.render(f"time (s): {round(time, 3)}", True, (255, 255, 255)), (0, 0))
        self.surface.blit(font.render(f"selected coords: {mouse_pos}", True, (255, 255, 255)), (0, 1*font.get_height()))
        self.surface.blit(font.render(f"object coords: {obj_pos}", True, (255, 255, 255)), (0, 2*font.get_height()))
        self.surface.blit(font.render(f"object vel: {obj_vel}", True, (255, 255, 255)), (0, 3*font.get_height()))
        self.surface.blit(font.render(f"object acc: {obj_acc}", True, (255, 255, 255)), (0, 4*font.get_height()))

        return self.surface