from classes.graphs import *
from algorithms.dijkstra import Dijkstra
from classes.models import RushHour
from itertools import product
import time
import tracemalloc

def dijkstra_many_times(board_size: int, board_file: str) -> None:
    """
    Run Dijkstra's algorithm multiple times with different parameters on the Rush Hour game.
    """
    
    board_name = board_file[19:-4]
    print(board_name)
    
    results: list[tuple[str, int, float, int]] = []
    iter_nums = [1, 10, 100, 1000, 10, 100, 1000, 10_000]
    cutoff_nums = [200_000, 20_000, 2_000, 200, 200_000, 20_000, 2_000, 200]

    tracemalloc.start()
    
    # Iterate over the iteration and cutoff numbers
    for iterations, cutoff in zip(iter_nums, cutoff_nums):
        for _ in range(3):
            start_time = time.time()
            dijkstras_algorithm = Dijkstra(board_size, board_file)
            dijkstras_algorithm.build_graph(iterations, cutoff)
            try:
                dijkstras_algorithm.run()
                move_nr = dijkstras_algorithm.export_solution(export_file=None)
            except IndexError:
                move_nr = 0
             
            # Get the peak memory usage   
            _, mem_peak = tracemalloc.get_traced_memory()
            results.append((f"{iterations=} {cutoff=}", move_nr, time.time() - start_time, mem_peak))
            tracemalloc.reset_peak()

    with open(f"results/output_dijkstra_test_{board_name}.csv", 'w') as file:
        file.write(f"parameters,moves,time,memory\n")
        for result in results:
            file.write(result[0]+f",{result[1]},{result[2]},{result[3]}\n")
