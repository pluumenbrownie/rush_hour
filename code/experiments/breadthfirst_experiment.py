from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst

import time
import statistics as stat

def breadth_first_experiment(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    Run the breadth-first search algorithm to determine the optimal solution for the Rush Hour game.
    """
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    
    for _ in range(repeat):
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        breadth_first_algorithm = BreadthFirst(game)
        breadth_first_algorithm.run()
        t = len(breadth_first_algorithm.visited_states)
        m = breadth_first_algorithm.best_move_count
        tries.append(t) 
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_breadth_first.csv")
   
    end_time = time.time()
    print(f"The breadth first algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/breadth_first_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")