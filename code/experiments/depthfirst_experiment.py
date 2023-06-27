from classes.models import RushHour
from algorithms.depth_first import DepthFirst

import time
import statistics as stat

def depth_first_experiment(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    Determine a random solution for the Rush Hour game.
    """
    start_time = time.time()
    n_runs = 0

    tries: list[int] = []
    moves: list[int] = []
    
    while time.time() - start_time < 5:
        print(f"run: {n_runs}")
        n_runs += 1
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        depth_first_algorithm = DepthFirst(game)
        depth_first_algorithm.run()
        t = len(depth_first_algorithm.visited_states)
        m = depth_first_algorithm.best_move_count
        
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_depth_first.csv")
   
    end_time = time.time()
    print(f"The depth first algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {n_runs} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/depth_first_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")
    