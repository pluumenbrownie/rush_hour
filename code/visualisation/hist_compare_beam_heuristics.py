import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def compare_plot(board: str) -> None:
    """
    Generate a bar plot comparing the means of the different heuristics from the beam search algorithm. 
    """
    
    # Read the data from the csv file
    h1_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h1_beam50.csv") 
    h2_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h2_beam50.csv") 
    h3_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h3_beam50.csv") 

    # Define the mean of each heuristic
    h1_mean = np.mean(h1_results)
    h2_mean = np.mean(h2_results)
    h3_mean = np.mean(h3_results)
 
    # Define the names of the algorithms and the mean values
    algorithms = ['Random', 'Random_optimized', 'Depth-First', 'Breadth_first'] 
    means = [h1_mean, h2_mean, h3_mean]

    # Create a bar plot
    plt.bar(algorithms, means)
    plt.xlabel('Algorithms')
    plt.ylabel('Mean')
    plt.title('Comparison of the means')
    plt.savefig(f'results/output{board}_compare_algorithms.png')