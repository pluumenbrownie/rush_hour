import matplotlib.pyplot as plt
import pandas as pd

from algorithms.algorithm import Algorithm as Algorithm

def histogram_plot(board):
    # Read the data from the csv file
    data = pd.read_csv(f"results/random_moves_{board}.csv")
    
    # Use the right parameters
    histogram = data.plot.hist(bins=100, column=['tries'])
    plot = histogram.get_figure()
    plot.savefig(f'results/output{board}_random_graph.png')
    
    