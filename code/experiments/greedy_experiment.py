from classes.models import RushHour
from algorithms.greedy import Greedy
import time
import statistics as stat

def determine_greedy_solution(board_size: int, board: str, export: bool = False):
    """
    Determine a semi random solution for the Rush Hour game using the greedy algorithm.

    The greedy algorithm is executed multiple times until one hour of execution time is reached.
    Statistics such as the number of tries and successful moves are collected and printed.
    """
    start_time = time.time()
    n_runs = 0

    tries: list[int] = []
    moves: list[int] = []
    while time.time() - start_time < 3600:
        print(f"run: {n_runs}")
        n_runs += 1
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        greedy_algorithm = Greedy(game)
        t, m = greedy_algorithm.run(export=False)
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_greedy.csv")
   
    end_time = time.time()
    print(f"The greedy algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {n_runs} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")

    # Open file to get all the moves
    with open(f"results/greedy/greedy_moves_{board}.csv", 'w') as file:
        file.write("moves\n")
        for value in moves:
            file.write(f"{value}\n")