from classes.models import RushHour
from algorithms.beam_search import BeamSearch

import time
import statistics as stat

def beam_search_experiment(board_size: int, board: str, repeat: int = 1, export: bool = False):
    """
    TO DO description
    """
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    
    for _ in range(repeat):
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        algorithm = BeamSearch(game)
        algorithm.run()
        t = len(algorithm.visited_states)
        m = algorithm.best_move_count
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_beam_search.csv")
   
    end_time = time.time()
    print(f"The beam search algorithm took {end_time - start_time:.3f} seconds.")

    # print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/beam_search_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")