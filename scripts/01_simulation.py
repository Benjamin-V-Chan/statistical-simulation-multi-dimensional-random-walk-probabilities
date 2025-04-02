import numpy as np
import csv
import os

def simulate_random_walk(dimension, num_steps):
    position = np.zeros(dimension, dtype=int)
    for step in range(1, num_steps + 1):
        axis = np.random.randint(0, dimension)
        move = np.random.choice([-1, 1])
        position[axis] += move
        if np.all(position == 0):
            return True
    return False

def main():
    dimensions = [1, 2, 3]
    num_steps = 1000
    num_trials = 10000
    output_dir = os.path.join("..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "simulation_results.csv")
    with open(output_file, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["dimension", "trial", "returned"])
        for dim in dimensions:
            for trial in range(1, num_trials + 1):
                returned = simulate_random_walk(dim, num_steps)
                writer.writerow([dim, trial, int(returned)])

if __name__ == "__main__":
    main()