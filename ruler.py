import pygame

from properties import *

class Ruler:
    def __init__(self, thickness, color) -> None:
        self.thickness = thickness
        self.color = color

        self.font_name = "sans-serif"
        self.font_size = 12

        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    def draw(self) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        pygame.draw.line(self.surface, self.color, (0, WIDTH), (WIDTH, HEIGHT), self.thickness) # horizontal line
        pygame.draw.line(self.surface, self.color, (0, 0), (0, HEIGHT), self.thickness) # vertical line

        font = pygame.font.SysFont(self.font_name, self.font_size)

        for x_scale_div_num in range(canvas_width):
            self.surface.blit(font.render(f"{x_scale_div_num}", False, self.color), (x_scale_div_num*pixels_in_meter, 500-15))
            pygame.draw.line(self.surface, pygame.Color(self.color.r//3, self.color.g//3, self.color.b//3), (x_scale_div_num*pixels_in_meter, 0), (x_scale_div_num*pixels_in_meter, HEIGHT))
            pygame.draw.line(self.surface, self.color, (x_scale_div_num*pixels_in_meter, HEIGHT), (x_scale_div_num*pixels_in_meter, HEIGHT-10))

        for y_scale_div_num in range(canvas_height):
            self.surface.blit(font.render(f"{canvas_height-y_scale_div_num}", False, self.color), (15, y_scale_div_num*pixels_in_meter))
            pygame.draw.line(self.surface, pygame.Color(self.color.r//3, self.color.g//3, self.color.b//3), (0, y_scale_div_num*pixels_in_meter), (WIDTH, y_scale_div_num*pixels_in_meter))
            pygame.draw.line(self.surface, self.color, (0, y_scale_div_num*pixels_in_meter), (10, y_scale_div_num*pixels_in_meter))

        return self.surface
