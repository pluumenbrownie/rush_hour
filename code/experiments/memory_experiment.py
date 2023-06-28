from algorithms.breadth_first import BreadthFirst
from algorithms.branch_and_bound import BranchAndBound
from algorithms.beam_search import BeamSearch
from classes.models import RushHour
import tracemalloc
from copy import deepcopy

def memory_comparison(board_size: int, board_file: str) -> None:
    tracemalloc.start()
    game = RushHour(board_size, board_file)
    algorithm = BreadthFirst(game)
    breadth_amount = algorithm.run()
    _, mem_peak_breadth = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    game = RushHour(board_size, board_file)
    algorithm = BranchAndBound(game, bound=100)
    branch_amount = algorithm.run(first_only=False)
    _, mem_peak_branch = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    beams = 50
    game = RushHour(board_size, board_file)
    algorithm = BeamSearch(game)
    beam_amount = algorithm.run('h2', beams)
    _, mem_peak_beam = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    print(f"Breadth first:    {mem_peak_breadth:12} Bytes, {breadth_amount:3} moves.")
    print(f"Branch and Bound: {mem_peak_branch:12} Bytes, {branch_amount:3} moves.")
    print(f"Beamsearch({beams}):   {mem_peak_beam:12} Bytes, {beam_amount:3} moves.")
