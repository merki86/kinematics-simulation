import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

gravity = 9.8

class Ball:
    def __init__(self) -> None:
        self.radius = 15
        self.color = (255, 255, 0)

        self.initial_position = (int(width/2-15), int(height/2-15))
        self.position_x = self.initial_position[0]
        self.position_y = self.initial_position[1]
        self.velocity = 0
        self.acceleration = gravity
    
    def draw(self) -> None:
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.radius)

ball = Ball()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # Render
    ball.draw()

    pygame.display.flip()

    # Logic
    time_passed = pygame.time.get_ticks() / 30 / 5

    new_position_y = int(1/2*ball.acceleration*(time_passed**2)) # h = 1/2*gt2

    if new_position_y >= height:
        new_position_y = height

    ball.position_y = new_position_y

    clock.tick(30)
    print(time_passed)

pygame.quit()