from classes.graphs import *
from algorithms.GraphBased import Dijkstra
from classes.models import RushHour

def dijkstra_many_times(board_size: int, board_file: str) -> None:
    move_list: list[int] = []
    settings = [80, 90, 100, 120, 140, 160, 180, 200, 240, 280, 300, 450, 500]

    for cutoff in settings:
        dijkstras_algorithm = Dijkstra(board_size, board_file)
        dijkstras_algorithm.build_graph(100_000, 1_000_000, 2000)
        dijkstras_algorithm.run()
        move_nr = dijkstras_algorithm.export_solution(export_file=None)
        move_list.append(move_nr)
    print(move_list)
