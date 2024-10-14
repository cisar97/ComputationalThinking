#! /usr/bin/env python3 

import random
import time
import os

start_time = time.time()

# Set the dimensions of the grid
width = 50
height = 20

# Create an empty grid
grid = [[False for _ in range(width)] for _ in range(height)]

# Initialize the grid with random live cells
for y in range(height):
    for x in range(width):
        grid[y][x] = random.choice([True, False])

# Function to print the current grid state
def print_grid():
    os.system('clear')  # Clears the terminal (for Unix-like systems)
    for row in grid:
        for cell in row:
            if cell:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()

# Function to count live neighbors for a cell
def count_neighbors(x, y):
    neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1),
                 (x-1, y),             (x+1, y),
                 (x-1, y+1), (x, y+1), (x+1, y+1)]
    count = 0
    for nx, ny in neighbors:
        if 0 <= nx < width and 0 <= ny < height:
            count += grid[ny][nx]
    return count

# Function to update the grid according to the rules of Conway's Game of Life
def update_grid():
    new_grid = [[False for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            live_neighbors = count_neighbors(x, y)
            if grid[y][x]:  # If the cell is currently alive
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[y][x] = True
            else:  # If the cell is currently dead
                if live_neighbors == 3:
                    new_grid[y][x] = True
    return new_grid

# Main loop to run the simulation
#while True:
for i in range(1000):
    print_grid()
    grid = update_grid()
    #time.sleep(0.2)  # Adjust the sleep duration to control the speed of the simulation

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")

