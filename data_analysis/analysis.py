import os
import pandas as pd
import pickle
import pygame
from typing import List, Tuple
import matplotlib.pyplot as plt

def read_array_from_file(filename):
    with open(filename, 'rb') as file:
        array = pickle.load(file)
    return array

def tupelize_pygame_list(py_list: List[pygame.Vector2] ) -> List[Tuple[float,float]]:
    return [(vec.x,vec.y) for vec in py_list]

directory = './data/il_test/'

# Get all files in the directory
files = os.listdir(directory)

data = {}  # Dictionary to store the data

for file in files:
    if file[0].isdigit():  # Check if the file starts with a digit
        file_path = os.path.join(directory, file)
        
        # Read the file and load the list of numbers
        with open(file_path, 'r') as f:
            numbers = tupelize_pygame_list(read_array_from_file(file_path))
        
        column_name = file.split('.')[0]  # Extract the file number as the column name
        
        data[column_name] = numbers

# Create the DataFrame
df = pd.DataFrame(data)

# Number of segments to cut the column into
num_segments = 15

# Calculate segment size
segment_size = len(df) // num_segments

# Plotting each segment of the column
for i in range(10,num_segments):
    start_index = i * segment_size
    end_index = (i + 1) * segment_size
    segment_data = df["3"].iloc[start_index:end_index]
    x = [item[0] for item in segment_data]
    y = [item[1] for item in segment_data]
    plt.plot(x, y, label=f'Segment {i+1}')

# Set plot title and labels
plt.title("Column Segments")
plt.xlabel("Index")
plt.ylabel("Value")

# Show legend
plt.legend()

# Display the plot
plt.show()
