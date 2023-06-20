from classes.models import RushHour
from algorithms.random import Random

import time
import statistics as stat

def determine_optimized_random_solution(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    Determine a random solution for the Rush Hour game.
    """
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    for _ in range(repeat):
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        random_algorithm = Random(game)
             
        t, m = random_algorithm.run(export=False)
        m = random_algorithm.optimize_random()

        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_random_optimized.csv")
   
    end_time = time.time() - start_time
    
    print(f"The random optimized algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/random_optimized_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")