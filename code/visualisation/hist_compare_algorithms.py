import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Stap 2: Definieer de resultaten van elk algoritme in een lijst
def compare_plot(board):
    
    # Read the data from the csv file
    random_results = pd.read_csv(f"results/random_moves_{board}.csv") 
    random_optimized_results = pd.read_csv(f"results/random_optimized_moves_{board}.csv")
    depth_first_results = pd.read_csv(f"results/depth_first_moves_{board}.csv")
    breadth_first_results = pd.read_csv(f"results/breadth_first_moves_{board}.csv")

    # Stap 3: Bereken het gemiddelde van elk algoritme
    random_mean = np.mean(random_results)
    random_optimized_mean = np.mean(random_optimized_results)
    depth_first_mean = np.mean(depth_first_results)
    breadth_first_mean = np.mean(breadth_first_results)

    # Stap 4: Definieer de namen van de algoritmes en het gemiddelde
    algorithms = ['Random', 'Random_optimized', 'Depth-First', 'Breadth_first'] 
    means = [random_mean, random_optimized_mean, depth_first_mean, breadth_first_mean]

    # Stap 5: Maak een bar plot
    plt.bar(algorithms, means)
    plt.xlabel('Algorithms')
    plt.ylabel('Mean')
    plt.title('Comparison of the means')
    plt.savefig(f'results/output{board}_compare_algorithms.png')