from algorithms.greedy import Greedy
from algorithms.random import Random
from algorithms.depth_first import DepthFirst
from algorithms.breadth_first import BreadthFirst
from classes.models import RushHour
from visualisation.histogram import histogram_plot
from classes.models import RushHour, count_statespace
from pygame_rushhour import PygameRushHour
from experiments.random_experiment import determine_random_solution
from sys import argv
  
if __name__ == '__main__':
    
    # Code to ask user for input, boardsize and algorithm    
    if len(argv) == 1:
      print("Usage: python3 code/main.py [boardsize] [boardfile] algorithm")
      exit(1)
    
    boardsize = int(argv[1])
    boardfile = argv[2]  
    game = RushHour(boardsize, boardfile)
    print("locatie van x")
    print(game.get_vehicle_from_location(2, 4))

    
# --------------------------------------------Algorithms--------------------------------------------#
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
            depthfirst_algorithm.run(first_only = True)
        elif argv[3] == "greedy":
            greedy_algorithm = Greedy(game)
            greedy_algorithm.run()
        elif argv[3] == "breadthfirst":
            breadthfirst_algorithm = BreadthFirst(game)
            breadthfirst_algorithm.run()
        elif argv[3] == "statespace":
            print(count_statespace(boardsize, boardfile))
        
        # Run this if you want to play the game yourself
        elif argv[3] == "play":
            game.start_game()
            
# --------------------------------------------Visualisation--------------------------------------------#
    # Make a plot of a histogram for random
    if len(argv) > 4 and argv[4] == "histogram":
        board = "6x6_1"
        determine_random_solution(boardsize, board, 100)
        histogram_plot(board)
    
    # Animate the game using pygame (only for random_optimized)
    elif len(argv) > 4 and argv[4] == "animate":
        results_file = "results/output_optimized.csv"
        newgame = PygameRushHour(boardsize, boardfile, results_file)
        newgame.start()