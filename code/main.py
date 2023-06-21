from algorithms.greedy import Greedy
from algorithms.random import Random
from algorithms.depth_first import DepthFirst
from algorithms.breadth_first import BreadthFirst
from algorithms.beam_search import BeamSearch
from classes.models import RushHour
from visualisation.histogram import histogram_plot
from visualisation.hist_compare_algorithms import compare_plot
from classes.models import RushHour, count_statespace
from pygame_rushhour import PygameRushHour
from experiments.random_experiment import determine_random_solution
from experiments.random_optimized_experiment import determine_optimized_random_solution
from experiments.breadthfirst_experiment import breadth_first_experiment
from experiments.depthfirst_experiment import depth_first_experiment


from sys import argv
  
if __name__ == '__main__':
    
    # Code to ask user for input, boardsize and algorithm    
    if len(argv) == 1:
      print("Usage: python3 code/main.py [boardsize] [boardfile] algorithm")
      exit(1)
    
    boardsize = int(argv[1])
    boardfile = argv[2]  
    game = RushHour(boardsize, boardfile)

    if len(argv) > 3:   
        if argv[3] == "random":
            random_algorithm = Random(game)
            random_algorithm.run()
        elif argv[3] == "random_optimized":
            random_algorithm = Random(game)
            random_algorithm.run()
            game.optimize_solution()
            game.export_solution(output_name="results/output_optimized.csv")
        elif argv[3] == "depthfirst":
            depthfirst_algorithm = DepthFirst(game)
            depthfirst_algorithm.run(first_only = False)
        elif argv[3] == "greedy":
            greedy_algorithm = Greedy(game)
            greedy_algorithm.run()
        elif argv[3] == "breadthfirst":
            breadthfirst_algorithm = BreadthFirst(game)
            breadthfirst_algorithm.run()
        elif argv[3] == "beamsearch":
            beamsearch_algorithm = BeamSearch(game)
            beamsearch_algorithm.run()
        elif argv[3] == "statespace":
            print(count_statespace(boardsize, boardfile))
        elif argv[3] == "compare":
            board = "6x6_1"
            determine_random_solution(boardsize, board, 15)
            determine_optimized_random_solution(boardsize, board, 15)
            breadth_first_experiment(boardsize, board, 15)
            depth_first_experiment(boardsize, board, 15)
            compare_plot(board)
        
        # Run this if you want to play the game yourself
        elif argv[3] == "play":
            game.start_game()
            
# --------------------------------------------Visualisation--------------------------------------------#
    # Make a plot of a histogram for random
    if len(argv) > 4 and argv[4] == "histogram":
        board = "6x6_1"
        if argv[3] == "random": # in histogram moet bij column['moves'] staan 
            determine_random_solution(boardsize, board, 1000)
            histogram_plot(f"results/random_moves_{board}.csv", f'results/output{board}_random_graph_moves.png')
        elif argv[3]== "random_optimized": # in histogram moet bij column['tries'] staan 
            determine_optimized_random_solution(boardsize, board, 1000)
            histogram_plot(f"results/random_optimized_moves_{board}.csv", f'results/output{board}_random_graph_optimized_moves.png')       
         
           
    # Animate the game using pygame (only for random_optimized)
    elif len(argv) > 4 and argv[4] == "animate":
        results_file = "results/output_optimized.csv"
        newgame = PygameRushHour(boardsize, boardfile, results_file)
        newgame.start()