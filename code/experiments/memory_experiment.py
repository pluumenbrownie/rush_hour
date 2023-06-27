from algorithms.breadth_first import BreadthFirst
from algorithms.branch_and_bound import BranchAndBound
from algorithms.beam_search import BeamSearch
from classes.models import RushHour
import tracemalloc
from copy import deepcopy

def memory_comparison(board_size: int, board_file: str) -> None:
    tracemalloc.start()
    game = RushHour(board_size, board_file)
    breadthfirst_algorithm = BreadthFirst(game)
    _, mem_peak = tracemalloc.get_traced_memory()
