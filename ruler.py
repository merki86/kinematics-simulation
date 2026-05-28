import pygame

from properties import *

class Ruler:
    def __init__(self, color) -> None:
        self.thickness = 1
        self.color = color

        self.font_name = "sans-serif"
        self.font_size = 14

        self.surface = pygame.Surface((canvas_width*pixels_in_meter+1, canvas_height*pixels_in_meter+1), pygame.SRCALPHA) # +1 because real visible surface is width-1; height-1

    def draw(self) -> pygame.Surface:
        self.surface.fill((0, 0, 0, 0))

        font = pygame.font.SysFont(self.font_name, self.font_size)

        for x_scale_div_num in range(canvas_width+1): # +1 because 0 -> n-1 range for canvas_width = n
            pygame.draw.line(self.surface, pygame.Color(self.color.r//3, self.color.g//3, self.color.b//3), (x_scale_div_num*pixels_in_meter, 0), (x_scale_div_num*pixels_in_meter, canvas_height*pixels_in_meter))
            pygame.draw.line(self.surface, self.color, (x_scale_div_num*pixels_in_meter, canvas_height*pixels_in_meter), (x_scale_div_num*pixels_in_meter, canvas_height*pixels_in_meter-10))
            self.surface.blit(font.render(f"{x_scale_div_num}", True, self.color), (x_scale_div_num*pixels_in_meter-10, canvas_height*pixels_in_meter-15))

        for y_scale_div_num in range(canvas_height+1):
            pygame.draw.line(self.surface, pygame.Color(self.color.r//3, self.color.g//3, self.color.b//3), (0, y_scale_div_num*pixels_in_meter), (canvas_width*pixels_in_meter, y_scale_div_num*pixels_in_meter))
            pygame.draw.line(self.surface, self.color, (0, y_scale_div_num*pixels_in_meter), (10, y_scale_div_num*pixels_in_meter))
            self.surface.blit(font.render(f"{abs(canvas_height-y_scale_div_num)}", True, self.color), (15, y_scale_div_num*pixels_in_meter))

        pygame.draw.line(self.surface, self.color, (0, canvas_width*pixels_in_meter), (canvas_width*pixels_in_meter, canvas_height*pixels_in_meter), self.thickness) # horizontal line
        pygame.draw.line(self.surface, self.color, (0, 0), (0, canvas_height*pixels_in_meter), self.thickness) # vertical line

        return self.surface
