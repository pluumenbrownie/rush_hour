from algorithms.greedy import Greedy
from algorithms.random import Random
from algorithms.depth_first import DepthFirst
from algorithms.breadth_first import BreadthFirst
from algorithms.branch_and_bound import BranchAndBound
from algorithms.beam_search import BeamSearch
from algorithms.GraphBased import Dijkstra
from classes.models import RushHour
from visualisation.histogram import histogram_plot
from visualisation.hist_compare_algorithms import compare_plot
from classes.models import RushHour, count_statespace
from classes.graphs import test
from pygame_rushhour import PygameRushHour
from experiments.random_experiment import determine_random_solution
from experiments.random_optimized_experiment import determine_optimized_random_solution
from experiments.breadthfirst_experiment import breadth_first_experiment
from experiments.depthfirst_experiment import depth_first_experiment
from experiments.beamsearch_experiment import beam_search_experiment

from sys import argv
  
if __name__ == '__main__':
    
    # Code to ask user for input, boardsize and algorithm    
    if len(argv) == 1:
        print("Usage: python3 code/main.py [boardsize] [boardfile] algorithm")
        exit(1)
    
    boardsize = int(argv[1])
    boardfile = argv[2]  
    game = RushHour(boardsize, boardfile)
    game.show_board()
    
    # To experiment add the board to the command
    board = "9x9_6"

    if len(argv) > 3:   
        if argv[3] == "random":
            random_algorithm = Random(game)
            random_algorithm.run()
        elif argv[3] == "random_optimized":
            random_algorithm = Random(game)
            random_algorithm.run()
            game.optimize_solution()
            game.export_solution()
        elif argv[3] == "depthfirst":
            depthfirst_algorithm = DepthFirst(game)
            depthfirst_algorithm.run(first_only = False)
        elif argv[3] == "greedy":
            greedy_algorithm = Greedy(game)
            greedy_algorithm.run()
        elif argv[3] == "breadthfirst":
            breadthfirst_algorithm = BreadthFirst(game)
            breadthfirst_algorithm.run()
        elif argv[3] == "branchandbound":
            branchandbound_algorithm = BranchAndBound(game, bound=185)
            # branchandbound_algorithm.bound_guess()
            branchandbound_algorithm.run(first_only = False, output_file="results/output_depthfirst_12x12_7.csv")
        elif argv[3] == "beamsearch":
            beamsearch_algorithm = BeamSearch(game)
            beamsearch_algorithm.run()
        elif argv[3] == "statespace":
            print(count_statespace(boardsize, boardfile))
        elif argv[3] == "compare":
            determine_random_solution(boardsize, board, 15)
            determine_optimized_random_solution(boardsize, board, 15)
            breadth_first_experiment(boardsize, board, 15)
            depth_first_experiment(boardsize, board, 15)
            compare_plot(board)
        elif argv[3] == "depth_exp":
            depth_first_experiment(boardsize, board, 1)
        elif argv[3] == "breadth_exp":
            breadth_first_experiment(boardsize, board, 1)
        elif argv[3] == "beam_exp":
            heuristic = 'h1'
            beam_search_experiment(boardsize, board, 10, heuristic)
        elif argv[3] == "graph":
            test(boardsize, boardfile)
        elif argv[3] == "dijkstra":
            dijkstras_algorithm = Dijkstra(boardsize, boardfile)
            dijkstras_algorithm.build_graph(150_000_000, 1000_000)
            dijkstras_algorithm.run()
            dijkstras_algorithm.export_solution()
        
        # Run this if you want to play the game yourself
        elif argv[3] == "play":
            game.start_game()
            
# --------------------------------------------Visualisation--------------------------------------------#
    # Make a plot of a histogram for random
    if len(argv) > 4 and argv[4] == "histogram":
        if argv[3] == "random": 
            determine_random_solution(boardsize, board, 100)
            histogram_plot(f"results/random_moves_{board}.csv", f'results/output{board}_random_graph_moves.png')
        elif argv[3]== "random_optimized":
            determine_optimized_random_solution(boardsize, board, 1000)
            histogram_plot(f"results/random_optimized_moves_{board}.csv", f'results/output{board}_random_graph_optimized_moves.png')     
        elif argv[3]== "beam":   
            beam_search_experiment(boardsize, board, 100)
            histogram_plot(f"results/beam_search/random_optimized_moves_{board}.csv", f'results/beam_search/output{board}_beamsearch.png')     

         
           
    # Animate every algorithm game using pygame
    elif len(argv) > 4 and argv[4] == "animate":
        results_file = "results/output.csv"
        newgame = PygameRushHour(boardsize, boardfile, results_file)
        newgame.start()