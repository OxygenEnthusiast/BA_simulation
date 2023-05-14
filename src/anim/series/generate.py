import argparse
import pickle
from math import sqrt, log


size = 100_000_000

theorem_function_map = {
        'no': lambda _: 1, 
        'slln': lambda n: n,
        'clt': lambda n: sqrt(n),
        'il': lambda n:  1 if (n <= 16) else sqrt(2* n * log(log(n))) 
        }

def write_array_to_file(array, filename):
    with open(filename, 'wb') as file:
        pickle.dump(array, file)

def main(theorem):

    divisor = theorem_function_map[theorem]

    # Generate the series
    series_array = [1 / divisor(n) for n in range(1, size + 1)]

    # Example usage
    file_name = f"{theorem}_array.pkl"

    # Write the array to file
    write_array_to_file(series_array, file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate sequences for division")
    parser.add_argument('theorem', type=str,choices=['no','il','clt','slln'], help='shortcut for theorem')
    args = parser.parse_args()
    main(args.theorem)




