from classes.models import RushHour
from algorithms.beam_search import BeamSearch

import time
import statistics as stat


def beamsearch_experiment(board_size: int, board: str, heuristic: str = 'h1', beam_size: str = 50, export: bool = False):
    """
    Experiment of beam search 
    """
    start_time = time.time()
    n_runs = 0

    tries: list[int] = []
    moves: list[int] = []

    # Each run lasts a maximum of 60 seconds and after 3600 seconds the whole thing stops
    while time.time() - start_time < 60:  
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        algorithm = BeamSearch(game)
        algorithm.run(heuristic, beam_size)
        # end_time = time.time()
        
        t = len(algorithm.visited_states)
        m = algorithm.best_move_count
        tries.append(t) 
        moves.append(m)
        n_runs += 1
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_beam_search_{heuristic}_beam{beam_size}.csv")
   
    # print(f"The beam search algorithm took {end_time - start_time:.3f} seconds.")

    # Open file to get all the moves
    with open(f"results/beam_search/beam_search_moves_{board}_{heuristic}_beam{beam_size}.csv", 'w') as file:
        # file.write(f"moves, running time\n")
        # for value1, value2 in zip(moves):
        #     file.write(f"{value1}, {value2:.3f}\n")
        file.write(f"moves\n")
        for move in moves:
            file.write(f"{move}\n")
        