from random import choice

class Walker:
    nums = []
    pos = 0

    def gen(self):
        new_random_number = choice([-1,1])
        self.nums.append(new_random_number)
        return new_random_number

    def walk(self):
        self.pos += self.gen()
