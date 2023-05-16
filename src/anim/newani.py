# Example file showing a circle moving on screen
import pygame
from .prewalker import Walker

class Animation:

    AMOUNT_OF_WALKERS = 10
    LENGTH_OF_SIMULATION = 1_000_000

    speed = 1000
    frames = 0
    running = True
    dt = 0
    iteration = 0


    def __init__(self, theorem):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.inital_walker_pos  = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.walkers = [Walker(theorem, self.LENGTH_OF_SIMULATION) for _ in range(self.AMOUNT_OF_WALKERS)]
        self.clock = pygame.time.Clock()
        # Set up the timer event
        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, self.speed)  # 1000 milliseconds = 1 second

    def increment_iteration(self):
        new_it = self.iteration + self.frames
        if (new_it < self.LENGTH_OF_SIMULATION):
            self.iteration = new_it


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.TIMER_EVENT:
                self.increment_iteration()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.frames += 1
                if event.key == pygame.K_DOWN:
                    self.frames -= 1
                if event.key == pygame.K_RIGHT:
                    self.frames += 100
                if event.key == pygame.K_LEFT:
                    self.frames -= 100
                self.frames = max(0, self.frames)
                if event.key == pygame.K_q:
                    self.speed = 50 if (self.speed == 1000) else 1000
                    pygame.time.set_timer(self.TIMER_EVENT, self.speed)  # 1000 milliseconds = 1 second

    
    def draw_figures(self):
        for walker in self.walkers:
            position = walker.transformed_path[self.iteration] + self.inital_walker_pos
            if (0 <= position.x <= self.screen.get_width() and
                0 <= position.y <= self.screen.get_height()):
                pygame.draw.circle(self.screen, walker.color , position , 5)

    def draw(self):
        self.handle_events()
        self.screen.fill("gray")
        pygame.draw.circle(self.screen, "lightgray", self.inital_walker_pos, 100)

        self.draw_figures()

        font = pygame.font.Font(None, 36)
        text = font.render(f"IPF: {self.frames} \n FPS: {1000//self.speed}", True, "black")
        self.screen.blit(text, (100 , 100 ))
        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000

    
