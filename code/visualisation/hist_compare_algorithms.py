import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def compare_plot(board: str) -> None:
    """
    Generate a bar plot comparing the means of different algorithms based on their results.
    """
    
    # Read the data from the csv file
    random_results = pd.read_csv(f"results/random_moves_{board}.csv") 
    random_optimized_results = pd.read_csv(f"results/random_optimized_moves_{board}.csv")
    depth_first_results = pd.read_csv(f"results/depth_first_moves_{board}.csv")
    breadth_first_results = pd.read_csv(f"results/breadth_first_moves_{board}.csv")

    # Calculate the mean of each algorithm
    random_mean = np.mean(random_results)
    random_optimized_mean = np.mean(random_optimized_results)
    depth_first_mean = np.mean(depth_first_results)
    breadth_first_mean = np.mean(breadth_first_results)

    # Define the names of the algorithms and the mean values
    algorithms = ['Random', 'Random_optimized', 'Depth-First', 'Breadth_first'] 
    means = [random_mean, random_optimized_mean, depth_first_mean, breadth_first_mean]

    # Create a bar plot
    plt.bar(algorithms, means)
    plt.xlabel('Algorithms')
    plt.ylabel('Mean')
    plt.title('Comparison of the means')
    plt.savefig(f'graphs/output{board}_compare_algorithms.png')