import pygame

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

time = 0
time_sec = 0
delta = 0
velocity = 0
is_fallen = False
displacement = 0

# Canvas
zoom = 50 # canvas cell's width and height in pixels
cell_x = 6
cell_y = 6
canvas_width = zoom * cell_x
canvas_height = zoom * cell_y

running = True

gravity = 9.8

class CoordinateSystem:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", size=16)

    def draw(self) -> None:
        # y axis
        # TODO: The other way
        y_point_division = canvas_height / cell_y
        pygame.draw.line(screen, (255, 0, 0), (0, 0), (0, canvas_height), 2)
        for point_number in range(cell_y):
            pygame.draw.line(screen, (255, 0, 0), (0, point_number*y_point_division), (20, point_number*y_point_division), 2)
            point_text = pygame.font.Font.render(self.font, f"{point_number}", False, (255, 0, 0))
            screen.blit(point_text, (25, point_number*y_point_division))

        # x axis
        x_point_division = canvas_width / cell_x
        pygame.draw.line(screen, (255, 0, 0), (0, canvas_height), (canvas_width, canvas_height), 2)
        for point_number in range(cell_x):
            pygame.draw.line(screen, (255, 0, 0), (point_number*x_point_division, canvas_height), (point_number*x_point_division, canvas_height+20), 2)
            point_text = pygame.font.Font.render(self.font, f"{point_number}", False, (255, 0, 0))
            screen.blit(point_text, (point_number*x_point_division, 25+canvas_height))

class Ball:
    def __init__(self) -> None:
        self.radius = 15
        self.color = (255, 255, 0)

        self.initial_position = (zoom*cell_x/2, zoom*cell_y)
        self.position_x = self.initial_position[0]
        self.position_y = self.initial_position[1]

        self.displacement = self.initial_position[1] - self.position_y # DELETE THIS
        self.velocity = 0
        self.acceleration = gravity
    
    def draw(self) -> None:
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.radius)

class Stopwatch:
    def __init__(self) -> None:
        self.multiplier = 1

        # MOVE
        self.font = pygame.font.SysFont("Arial", size=24)

    def draw(self) -> None:
        output_time_elapsed = pygame.font.Font.render(self.font, f"Time elapsed (s): {time_sec}", False, (255, 255, 255))
        output_delta = pygame.font.Font.render(self.font, f"Delta: {delta}", False, (255, 255, 255))
        output_velocity = pygame.font.Font.render(self.font, f"Velocity: {velocity}", False, (255, 255, 255))        
        output_displacement = pygame.font.Font.render(self.font, f"Displacement: {displacement}", False, (255, 255, 255))        
        output_fallen = pygame.font.Font.render(self.font, f"Is fallen: {is_fallen}", False, (255, 255, 255))

        screen.blit(output_time_elapsed, (0, 0))
        screen.blit(output_delta, (0, output_time_elapsed.get_rect().height))
        screen.blit(output_velocity, (0, output_time_elapsed.get_rect().height * 2))
        screen.blit(output_displacement, (0, output_time_elapsed.get_rect().height * 3))
        screen.blit(output_fallen, (0, output_time_elapsed.get_rect().height * 4))

ball = Ball()
stopwatch = Stopwatch()
coordinate_system = CoordinateSystem()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # Render
    ball.draw()
    stopwatch.draw()
    coordinate_system.draw()

    pygame.display.flip()

    # Logic

    # ANOTHER EQUATION
    new_position_y = int( 0.5*ball.acceleration*(time_sec**2) * 100 ) # h = 1/2*gt2 100 HERE IS 100 px = 1 m

    if new_position_y >= canvas_height:
        new_position_y = canvas_height
        is_fallen = True

    ball.position_y = new_position_y
    ball.displacement_y = ball.initial_position[1] - ball.position_y # DELETE THIS

    delta = clock.tick(60)
    time += delta
    time_sec = time / 1000
    # velocity = math.sqrt(velocity**2 + 2*ball.acceleration*ball.displacement_y)

# MAKE A RED LINE DETERMINING THE 0 SURFACE. THE TOP IS 6 m FOR INSTANCE. 600px
pygame.quit()