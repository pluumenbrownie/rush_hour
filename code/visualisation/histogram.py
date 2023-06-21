import matplotlib.pyplot as plt
import pandas as pd

# from algorithms.algorithm import Algorithm as Algorithm

def histogram_plot(path_board, path_output):
    # Read the data from the csv file
    data = pd.read_csv(path_board)
    
    # Use the right parameters
    histogram_t = data.plot.hist(bins=100, column=['moves'])
    plot_t = histogram_t.get_figure()
    plot_t.savefig(path_output)

