from classes.models import RushHour
from algorithms.beam_search import BeamSearch

import time
import statistics as stat

def beam_search_experiment(board_size: int, board: str, repeat: int = 1, export: bool = False, heuristic: str = 'h1', beam: str = 50):
    """
    TO DO description
    """
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    runtimes: list[int] = []

    for _ in range(repeat):
        start_time = time.time()
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        algorithm = BeamSearch(game)
        algorithm.run(heuristic)
        end_time = time.time()
        
        t = len(algorithm.visited_states)
        m = algorithm.best_move_count
        r = end_time - start_time
        tries.append(t) 
        moves.append(m)
        runtimes.append(r)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_beam_search_{heuristic}_beam{beam}.csv")
   
   
    print(f"The beam search algorithm took {end_time - start_time:.3f} seconds.")

    # print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/beam_search/beam_search_moves_{board}_{heuristic}_beam{beam}.csv", 'w') as file:
        file.write(f"moves, running time\n")
        for value1, value2 in zip(moves, runtimes):
            file.write(f"{value1}, {value2:.3f}\n")