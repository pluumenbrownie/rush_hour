import matplotlib.pyplot as plt
import pandas as pd
import os

# from algorithms.algorithm import Algorithm as Algorithm

def histogram_plot(board):
    # Read the data from the csv file
    data = pd.read_csv(f"results/random_moves_{board}.csv")
    
    # Use the right parameters
    histogram_t = data.plot.hist(bins=100, column=['tries'])
    plot_t = histogram_t.get_figure()
    plot_t.savefig(f'results/output{board}_random_graph_tries.png')
    
    # Make histogram for valid moves
    # histogram_m = data.plot.hist(bins=100, column=['moves'])
    # plot_m = histogram_m.get_figure()
    # plot_m.savefig(f'results/output{board}_random_graph_moves.png')

