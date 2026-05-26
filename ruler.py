import pygame

class Ruler:
    def __init__(self) -> None:
        pass

    def draw(self):
        surface = pygame.Surface((500, 500))

        pygame.draw.line(surface, (255, 0, 0), (0, 500), (500, 500), 5) # horizontal line
        pygame.draw.line(surface, (255, 0, 0), (0, 0), (0, 500), 5) # vertical line

        font = pygame.font.SysFont("sans-serif", 12)
        for x_scale_div_num in range(50):
            surface.blit(font.render(f"{x_scale_div_num}", False, (255, 0, 0)), (x_scale_div_num*10, 500-15))
            pygame.draw.line(surface, (255, 0, 0), (x_scale_div_num*10, 500), (x_scale_div_num*10, 500-10))

        for y_scale_div_num in range(50):
            surface.blit(font.render(f"{50-y_scale_div_num}", False, (255, 0, 0)), (15, y_scale_div_num*10))
            pygame.draw.line(surface, (255, 0, 0), (0, y_scale_div_num*10), (10, y_scale_div_num*10))

        return surface