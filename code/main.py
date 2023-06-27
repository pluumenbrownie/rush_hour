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
from experiments.greedy_experiment import determine_greedy_solution
from experiments.beamsearch_experiment import beamsearch_experiment
from experiments.dijkstra_experiment import dijkstra_many_times

from sys import argv
  
if __name__ == '__main__':
    
    # Code to ask user for input, boardsize and algorithm    
    if len(argv) == 1:
        print("Usage: python3 code/main.py [boardsize] gameboards/[boardfile] algorithm")
        exit(1)
    
    boardsize = int(argv[1])
    boardfile = argv[2]  
    game = RushHour(boardsize, boardfile)
    game.show_board()
    
    # To experiment add the board to the command 
    board = "9x9_4"

    if len(argv) > 3:   
        # Running the random algorithm 
        if argv[3] == "random":
            random_algorithm = Random(game)
            random_algorithm.run()

        # Getting a plot of running the random algorithm 
        elif argv[3] == "randomplt":
            histogram_plot(f"results/random_moves_{board}.csv", f'results/output{board}_random_graph_moves.png')

        # Running the greedy algorithm 
        elif argv[3] == "greedy":
            greedy_algorithm = Greedy(game)
            greedy_algorithm.run()

        # Getting a plot of running the greedy algorithm 
        elif argv[3] == "greedyplt":
            histogram_plot(f"results/greedy_moves_{board}.csv", f'results/output{board}_greedy_graph_moves.png')       
        
        # Running the random optimized algorithm 
        elif argv[3] == "random_optimized":
            random_algorithm = Random(game)
            random_algorithm.run()
            game.optimize_solution()
            game.export_solution()

        # Running the depth first search algorithm 
        elif argv[3] == "depthfirst":
            depthfirst_algorithm = DepthFirst(game)
            depthfirst_algorithm.run(first_only = False)

        # Running the breadth first search algorithm
        elif argv[3] == "breadthfirst":
            breadthfirst_algorithm = BreadthFirst(game)
            breadthfirst_algorithm.run()

        # Running the brand and bound algorithm 
        elif argv[3] == "branchandbound":
            branchandbound_algorithm = BranchAndBound(game, bound=185)
            # branchandbound_algorithm.bound_guess()
            branchandbound_algorithm.run(first_only = False, output_file="results/output_depthfirst_12x12_7.csv")
        
        # Running the beam search algorithm
        elif argv[3] == "beamsearch":
            beamsearch_algorithm = BeamSearch(game)
            if argv[4] == 'h1': 
                heuristic = 'h1'
            elif argv[4] == 'h2': 
                heuristic = 'h2'
            elif argv[4] == 'h3': 
                heuristic = 'h3'
            beam_size = argv[5]
            beamsearch_algorithm.run(heuristic, beam_size)

        # Calculating the statespace  
        elif argv[3] == "statespace":
            print(count_statespace(boardsize, boardfile))

        # Compare plot for the practice presentation 
        elif argv[3] == "compare":
            determine_random_solution(boardsize, board, 15)
            determine_optimized_random_solution(boardsize, board, 15)
            breadth_first_experiment(boardsize, board, 15)
            depth_first_experiment(boardsize, board, 15)
            compare_plot(board)
        
        # Running the depth first search experiment 
        elif argv[3] == "depth_exp":
            depth_first_experiment(boardsize, board, 1)

        # Running the breadth first search experiment 
        elif argv[3] == "breadth_exp":
            breadth_first_experiment(boardsize, board, 1)

        # Running the beam search experiment (python3 code/main.py 6 gameboards/Rushhour6x6_1.csv beam_exp)
        elif argv[3] == "beam_exp":
            beamsearch_experiment(boardsize, board)

        # Creating a test graph 
        elif argv[3] == "graph":
            test(boardsize, boardfile)
        
        # Running the dijkstra algorithm
        elif argv[3] == "dijkstra":
            dijkstras_algorithm = Dijkstra(boardsize, boardfile)
            dijkstras_algorithm.build_graph(100_000, 1_000_000, 2000)
            dijkstras_algorithm.run()
            dijkstras_algorithm.export_solution()

        # Running a test of dijkstra 
        elif argv[3] == "dijkstra_test":
            dijkstra_many_times(boardsize, boardfile)
    
        # Run this if you want to play the game yourself
        elif argv[3] == "play":
            game.start_game()

    # --------------------------------------------Visualisation--------------------------------------------#
    # Make a plot of a histogram for random
    if len(argv) > 4 and argv[4] == "histogram":
        if argv[3] == "random": 
            determine_random_solution(boardsize, board, 50)
            histogram_plot(f"results/random_moves_{board}.csv", f'results/output{board}_random_graph_moves.png')
        elif argv[3]== "random_optimized":
            determine_optimized_random_solution(boardsize, board, 1000)
            histogram_plot(f"results/random_optimized_moves_{board}.csv", f'results/output{board}_random_graph_optimized_moves.png')
        elif argv[3] == "greedy":
            determine_greedy_solution(boardsize, board, 10)
            histogram_plot(f"results/greedy_moves_{board}.csv", f'results/output{board}_greedy_graph_moves.png')                
           
    # Animate every algorithm game using pygame
    elif len(argv) > 4 and argv[4] == "animate":
        results_file = "results/output.csv"
        newgame = PygameRushHour(boardsize, boardfile, results_file)
        newgame.start()