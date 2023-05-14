# Example file showing a circle moving on screen
import pygame, pickle
from .walker import Walker
from time import sleep

class Animation:

    AMOUNT_OF_WALKERS = 100
    speed = 1000
    frames = 0
    running = True
    dt = 0
    iteration = 0

    def read_array_from_file(self, filename):
        with open(filename, 'rb') as file:
            array = pickle.load(file)
        return array

    def create_walkers(self):
        self.walkers = [Walker(self.inital_walker_pos.copy()) for _ in range(self.AMOUNT_OF_WALKERS)]

    def __init__(self, theorem):
        pygame.init()
        self.theorem = self.read_array_from_file(f"./anim/series/{theorem}_array.pkl")
        self.screen = pygame.display.set_mode((1280, 720))
        self.inital_walker_pos  = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.create_walkers()
        self.clock = pygame.time.Clock()
        # Set up the timer event
        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, self.speed)  # 1000 milliseconds = 1 second

    def transform_walkers(self, walker_pos):
        res = self.inital_walker_pos + (walker_pos - self.inital_walker_pos) * self.theorem[self.iteration]
        # res = self.inital_walker_pos + (walker_pos - self.inital_walker_pos) / 1000
        return res

    def draw_figures(self):
        for walker in self.walkers:
            position = self.transform_walkers(walker.pos) 
            if (0 <= position.x <= self.screen.get_width() and
                0 <= position.y <= self.screen.get_height()):
                pygame.draw.circle(self.screen, walker.color , position , 5)

    def walk_walkers(self):
        self.iteration += self.frames
        for  walker in self.walkers:
            for _ in range(self.frames):
                walker.walk()

    def terminate(self):
        self.running = False
        for walker in self.walkers:
            pass
            # walker.terminate()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminate()
            elif event.type == self.TIMER_EVENT:
                self.walk_walkers()
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

    
