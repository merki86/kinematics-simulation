import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

time = 0
time_sec = 0
delta = 0

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

class Stopwatch:
    def __init__(self) -> None:
        self.multiplier = 1

        self.font = pygame.font.SysFont("Arial", size=32)

    def draw(self, delta: int) -> None:
        output = pygame.font.Font.render(self.font, f"Time elapsed (s): {time_sec} Delta: {delta}", False, (255, 255, 255))
        screen.blit(output, (0,height - output.get_rect().height))

ball = Ball()
stopwatch = Stopwatch()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # Render
    ball.draw()
    stopwatch.draw(delta)

    pygame.display.flip()

    # Logic

    new_position_y = int( 0.5*ball.acceleration*(time_sec**2) * 100 ) # h = 1/2*gt2 100 HERE IS 100 px = 1 m

    if new_position_y >= height:
        new_position_y = height

    ball.position_y = new_position_y

    delta = clock.tick(60)
    time += delta
    time_sec = time / 1000

pygame.quit()