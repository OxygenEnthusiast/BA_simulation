# Example file showing a circle moving on screen
import pygame, math
from .walker import Walker

class Animation:

    AMOUNT_OF_WALKERS = 100
    speed = 1
    running = True
    dt = 0
    iteration = 1

    theorem_function_map = {
            'no': lambda n: 100, 
            'slln': lambda n: n,
            'clt': lambda n: math.sqrt(n),
            'il': lambda n: math.sqrt(2 * (n + 16) * math.log(math.log(n + 16)))
            }

    def create_walkers(self):
        self.walkers = [Walker(self.inital_walker_pos.copy()) for _ in range(self.AMOUNT_OF_WALKERS)]

    def __init__(self, theorem):
        pygame.init()
        self.theorem = self.theorem_function_map[theorem]
        self.screen = pygame.display.set_mode((1280, 720))
        self.inital_walker_pos  = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.clock = pygame.time.Clock()
        self.create_walkers()
        # Set up the timer event
        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, self.speed)  # 1000 milliseconds = 1 second

    def transform_walkers(self, walker_pos):
        res = self.inital_walker_pos + (walker_pos - self.inital_walker_pos) / self.theorem(self.iteration)
        print(res)
        return res

    def draw_figures(self):
        for walker in self.walkers:
            pygame.draw.circle(self.screen, walker.color , self.transform_walkers(walker.pos) , 5)

    def walk_walkers(self):
        self.iteration += 1
        for  walker in self.walkers:
            walker.walk()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
           # elif event.type == self.TIMER_EVENT:
           #     self.walk_walkers()

    def draw(self):
        self.handle_events()
        self.walk_walkers()
        self.screen.fill("gray")
        pygame.draw.circle(self.screen, "lightgray", self.inital_walker_pos, 100)
        self.draw_figures()
        pygame.display.flip()
        self.dt = self.clock.tick(240) / 1000

    
