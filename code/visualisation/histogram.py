import matplotlib.pyplot as plt
import pandas as pd
import os

from classes.models import RushHour
from algorithms.random import Random
from algorithms.depth_first import DepthFirst
from algorithms.greedy3 import Greedy3
from algorithms.breadth_first import BreadthFirst


# from algorithms.algorithm import Algorithm as Algorithm

# def histogram_plot(board):
#     # Read the data from the csv file
#     data = pd.read_csv(f"results/random_moves_{board}.csv")
    
#     # Use the right parameters
#     histogram_t = data.plot.hist(bins=100, column=['tries'])
#     plot_t = histogram_t.get_figure()
#     plot_t.savefig(f'results/output{board}_random_graph_tries.png')
    
#     # Make histogram for valid moves
#     # histogram_m = data.plot.hist(bins=100, column=['moves'])
#     # plot_m = histogram_m.get_figure()
#     # plot_m.savefig(f'results/output{board}_random_graph_moves.png')
    
class Histogram:
    def __init__(self, board, algorithm):
        self.board = board
        self.algorithm = algorithm

    def plot(self):
        # Read the data from the csv file
        filename = f"results/{self.algorithm}_{self.board}.csv"
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Results file '{filename}' not found.")

        data = pd.read_csv(filename)

        # Plot histogram for 'tries'
        histogram_t = data.plot.hist(bins=100, column='tries')
        plot_t = histogram_t.get_figure()
        plot_t.savefig(f'results/output_{self.algorithm}_{self.board}_moves.png')
        
    def histogram_plot(self,board, algorithm):
        game = RushHour(6, f"gameboards/Rushhour{board}.csv")

        if algorithm == "random":
            random_algorithm = Random(game)
            random_algorithm.run()
        elif algorithm == "depthfirst":
            depthfirst_algorithm = DepthFirst(game)
            depthfirst_algorithm.run(first_only=True)
        elif algorithm == "greedy":
            greedy3_algorithm = Greedy3(game)
            greedy3_algorithm.run()
        elif algorithm == "breadthfirst":
            breadthfirst_algorithm = BreadthFirst(game)
            breadthfirst_algorithm.run()

        hist = Histogram(board, algorithm)
        hist.plot()