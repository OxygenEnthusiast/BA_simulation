from random import choice, randint
import pygame

class Walker:

    nums = []

    def __init__(self, pos) -> None:
        self.pos = pos
        self.color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

    def gen(self):
        random_x_step, random_y_step = choice([-1,1]),choice([-1,1])
        self.nums.append((random_x_step, random_y_step))
        return pygame.Vector2(random_x_step,random_y_step)

    def walk(self):
        self.pos += self.gen()
