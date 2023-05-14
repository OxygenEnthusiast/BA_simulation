import pickle
from random import choice

size = 1_000

def read_array_from_file(filename):
    with open(filename, 'rb') as file:
        array = pickle.load(file)
    return array

def write_array_to_file(array, filename):
    with open(filename, 'wb') as file:
        pickle.dump(array, file)

divisor = read_array_from_file("il_array.pkl")

x_seq = [choice([-1,1]) for _ in range(size)]

opath = [sum(x_seq[:n]) for n in range(1, len(x_seq) +1)]

scaled_path = [opath[n]*divisor[n] for n in range(len(opath))]

write_array_to_file(scaled_path, "il_path.pkl")
