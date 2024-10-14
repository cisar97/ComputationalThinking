#! /usr/bin/env python3 

import numpy as np
import os
import time

start_time = time.time()

# Create the grid and initialize it with random values
height, width = 20, 50
grid = np.random.choice([0, 1], size=(height, width), p=[0.8, 0.2])

# Function to print the current grid state
def print_grid():
    os.system('clear')  # Clears the terminal (for Unix-like systems)
    for row in grid:
        for cell in row:
            if cell == 1:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()


# Create an array to store neighbor counts
neighbor_counts = np.zeros_like(grid)

# Function to compute and store neighbor counts
def compute_neighbor_counts():
    for y in range(height):
        for x in range(width):
            # Count neighbors for each cell and store the result
            live_neighbors = np.sum(grid[max(0, y - 1):min(height, y + 2), max(0, x - 1):min(width, x + 2)]) - grid[y, x]
            neighbor_counts[y, x] = live_neighbors

# Initial computation of neighbor counts
compute_neighbor_counts()

# Function to update the grid based on neighbor counts
def update_grid():
    new_grid = np.copy(grid)
    for y in range(height):
        for x in range(width):
            live_neighbors = neighbor_counts[y, x]
            if grid[y, x]:  # If the cell is currently alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[y, x] = 0  # Cell dies
            else:  # If the cell is currently dead
                if live_neighbors == 3:
                    new_grid[y, x] = 1  # Cell becomes alive
    return new_grid

# Main simulation loop
#while True:
for i in range(1000):
    # Update the grid based on the neighbor counts
    grid = update_grid()

    # Re-compute neighbor counts for the next iteration
    compute_neighbor_counts()

    # Add your visualization code here
    #print_grid()
    #time.sleep(0.2)  # Adjust the sleep duration to control the speed of the simulation

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")

