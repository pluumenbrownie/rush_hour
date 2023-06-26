import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Stap 2: Definieer de resultaten van elk algoritme in een lijst
def compare_plot(board):
    
    # Read the data from the csv file
    h1_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h1_beam50.csv") 
    h2_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h2_beam50.csv") 
    h3_results = pd.read_csv(f"results/beam_search/beam_search_moves_6x6_1_h3_beam50.csv") 
    
    # random_optimized_results = pd.read_csv(f"results/random_optimized_moves_{board}.csv")
    # depth_first_results = pd.read_csv(f"results/depth_first_moves_{board}.csv")
    # breadth_first_results = pd.read_csv(f"results/breadth_first_moves_{board}.csv")

    # Stap 3: Bereken het gemiddelde van elke heuristiek
    h1_mean = np.mean(h1_results)
    h2_mean = np.mean(h2_results)
    h3_mean = np.mean(h3_results)
 
    # Stap 4: Definieer de namen van de algoritmes en het gemiddelde
    algorithms = ['Random', 'Random_optimized', 'Depth-First', 'Breadth_first'] 
    means = [h1_mean, h2_mean, h3_mean]

    # Stap 5: Maak een bar plot
    plt.bar(algorithms, means)
    plt.xlabel('Algorithms')
    plt.ylabel('Mean')
    plt.title('Comparison of the means')
    plt.savefig(f'results/output{board}_compare_algorithms.png')