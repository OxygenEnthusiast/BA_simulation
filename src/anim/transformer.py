from math import log, sqrt
from .file_handler import FileHandler
import pickle


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def write_array_to_file(array, filename):
    with open(filename, 'wb') as file:
        pickle.dump(array, file)


@singleton
class Transformer:

    theorem_function_map = {
            'no': lambda _: 1, 
            'slln': lambda n: n,
            'clt': lambda n: sqrt(n),
            # 'il': lambda n:  1 if (n <= 16) else sqrt(2* n * log(log(n))) 
            'il': lambda n:  sqrt(2* (n+16) * log(log(n+16))) 
            }

    def __init__(self, theorem, length) -> None:

        self.length = length

        self.theorem = theorem
        
        f = self.theorem_function_map[theorem]

        # Generate the series
        self.divisor = [1 / f(n) for n in range(1, length + 1)]

        print("generated divisor")

        file_handler = FileHandler(theorem)
        file_handler.write_array_to_file(self.divisor, "div")
        # Write the array to file
        #write_array_to_file(self.divisor, f"anim/series/{theorem}_divisor.pkl")

    def transform_walker(self, path):
        scaled_path = [path[n]*self.divisor[n] for n in range(self.length)]
        # write_array_to_file(scaled_path, f"anim/series/{datetime.now()}_{self.theorem}_{walker.number}.pkl")
        return scaled_path

