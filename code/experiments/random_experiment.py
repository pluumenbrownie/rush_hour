from classes.models import RushHour
from algorithms.random import Random

import time
import subprocess
import statistics as stat

def determine_random_solution(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    Determine a random solution for the Rush Hour game.
    """
    start_time = time.time()
    n_runs = 0

    # while time.time() - start_time < 3600:
    #     print(f"run: {n_runs}")
    #     # subprocess.call(["timeout", "60", "python3", "main.py", "random_algorithm.py",])
    #     n_runs += 1
    
    tries: list[int] = []
    moves: list[int] = []
    while time.time() - start_time < 3600:
        print(f"run: {n_runs}")
        n_runs += 1
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        random_algorithm = Random(game)
        t, m = random_algorithm.run(export=False)
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_random.csv")
   
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/random_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")