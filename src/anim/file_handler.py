import pickle
import os
from datetime import datetime


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class FileHandler:


    def __init__(self, theorem) -> None:
        ROOT_DIR = "anim/series/"
        self.dir = f"{ROOT_DIR}{theorem}_{datetime.now().strftime('%Y_%m_%d_%H:%M:%S')}/"
        os.mkdir(self.dir)


    def write_array_to_file(self, array, filename):
        with open(self.dir + str(filename) + ".pkl", 'wb') as file:
            pickle.dump(array, file)


    def read_array_from_file(self, filename):
        with open(self.dir + str(filename), 'rb') as file:
            array = pickle.load(file)
        return array
