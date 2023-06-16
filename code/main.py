from algorithms.algorithm import Algorithm
from algorithms.greedy2 import Greedy2
from algorithms.greedy3 import Greedy3
from algorithms.random import Random
from classes.models import RushHour
from visualisation.histogram import histogram_plot
from pygame_rushhour import PygameRushHour

import time
import statistics as stat


def determine_random_solution(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    Determine a random solution for the Rush Hour game.
    """
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    for _ in range(repeat):
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        random_algorithm = Random(game)
        t, m = random_algorithm.solve(export=False)
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_random.csv")
   
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the tries
    with open(f"results/random_moves_{board}.csv", 'w') as file:
        file.write("tries\n")
        for value in tries:
            file.write(f"{value}\n")
        
if __name__ == '__main__':
    
    # Code to ask user for input, boardsize and algorithm
    # from sys import argv
    
    # if len(argv) == 1:
    #   print("Usage: python3 code/main.py boardsize algorithm")
    
    # gameboard = argv[1]
    
    # if len(argv) > 2:
    #     if argv[2] == "random":
    #           run_algorithm(random)
     
    game = RushHour(6, "gameboards/Rushhour6x6_test.csv")
    # game = RushHour(6, "gameboards/Rushhour6x6_1.csv")
    # game = RushHour(12, "gameboards/Rushhour12x12_7.csv")

    
    # Run this if you want to play the game yourself
    # game.start_game()

    # Run this if you want to run the random algorithm
    random_algorithm = Random(game)
    random_algorithm.solve()

    # # Run this if you want to run the greedy2 (Dionne's implementation) algorithm
    # # greedy2_algorithm = Greedy2(game)
    # # greedy2_algorithm.solve()

    # # Run this if you want to run the greedy3 (Dionne's implementation) algorithm
    # greedy3_algorithm = Greedy3(game)
    # greedy3_algorithm.solve()
    
    # Make a plot of an histogram
    board = "6x6_1"
    determine_random_solution(6, board, 100)
    histogram_plot(board)

    # Make the visualisation
    board_file = "gameboards/Rushhour6x6_1.csv"
    newgame = PygameRushHour(6, board_file)
    newgame.start()