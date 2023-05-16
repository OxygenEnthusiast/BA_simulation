import pygame
from random import choice, randint
from datetime import datetime
from .transformer import Transformer
from .file_handler import FileHandler


class Walker:
    counter = 0

    def __init__(self, theorem,  length) -> None:
        self.number = Walker.counter
        Walker.counter += 1

        self.file_handler = FileHandler(f"{theorem}")

        self.color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

        self.length = length

        random_steps = self.generate_random_steps()

        self.path = self.generate_path(random_steps)

        transformer = Transformer(theorem, length)

        self.transformed_path =  transformer.transform_walker(self.path)

        print(f"generated path for {self.number}")
        #write_array_to_file(self.transformed_path, f"anim/series/{datetime.now()}_{theorem}_{self.number}.pkl")
        self.file_handler.write_array_to_file(self.transformed_path, self.number)

    def generate_random_steps(self):
        x_seq = [choice([-100,100]) for _ in range(self.length)]
        y_seq = [choice([-100,100]) for _ in range(self.length)]
        return (x_seq, y_seq)
        #return  [pygame.Vector2(x,y) for x,y in zip(x_seq,y_seq)]

    def generate_path(self, seq):
        x_path = list(self.partial_sums(seq[0]))
        y_path = list(self.partial_sums(seq[1]))
        return  [pygame.Vector2(x,y) for x,y in zip(x_path,y_path)]


    @staticmethod
    def partial_sums(original_sequence):
        cur = 0
        for value in original_sequence:
            yield cur
            cur += value

