import matplotlib.pyplot as plt
import pandas as pd

def histogram_plot(path_board: str, path_output: str):
    # Read the data from the csv file
    data = pd.read_csv(path_board)
    
    # Adjust moves greater than 50,000 to 50,000
    data.loc[data['moves'] > 50000, 'moves'] = 50000

    # Calculate total moves and mean
    moves = data['moves']
    data_total = len(moves)
    data_mean = moves.mean()

    # Plot the histogram
    histogram_t = data.plot.hist(bins=100, column=['moves'])
    plot_t = histogram_t.get_figure()

    # Add total runs and mean to the plot
    plt.text(0.30, 0.90, f"Mean: {data_mean:.2f}", transform=plot_t.transFigure)
    plt.text(0.50, 0.90, f"|  Total runs: {data_total:.2f}", transform=plot_t.transFigure)

    # Save and show the plot
    plot_t.savefig(path_output)
