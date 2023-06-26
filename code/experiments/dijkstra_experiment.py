from classes.graphs import *
from algorithms.GraphBased import Dijkstra
from classes.models import RushHour
from itertools import product
import time

def dijkstra_many_times(board_size: int, board_file: str) -> None:
    board_name = board_file[19:-4]
    print(board_name)
    results: list[tuple[str, int, float]] = []
    # move_list: list[int] = []
    # times: list[float] = []
    # settings = [80, 90, 100, 120, 140, 160, 180, 200, 240, 280, 300, 450, 500]
    iter_nums = [5000, 10_000, 20_000, 50_000]
    cutoff_nums = [50, 100, 150, 200]

    for iterations, cutoff in product(iter_nums, cutoff_nums):
        for _ in range(10):
            start_time = time.time()
            dijkstras_algorithm = Dijkstra(board_size, board_file)
            dijkstras_algorithm.build_graph(iterations, 1_000_000, cutoff)
            try:
                dijkstras_algorithm.run()
                move_nr = dijkstras_algorithm.export_solution(export_file=None)
            except IndexError:
                move_nr = 0
            results.append((f"{iterations=} {cutoff=}", move_nr, time.time() - start_time))

    with open(f"results/dijkstra_test_{board_name}.csv", 'w') as file:
        # file.write(f"moves, running time\n")
        # for value1, value2 in zip(moves):
        #     file.write(f"{value1}, {value2:.3f}\n")
        file.write(f"parameters,moves,time\n")
        for result in results:
            file.write(result[0]+f",{result[1]},{result[2]}\n")
