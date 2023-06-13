from algorithms.algorithm import Algorithm
from classes.models import RushHour
import time
import statistics as stat


def determine_random_solution(board_size: int, board: str, repeat: int = 1, export: bool = False):
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    for _ in range(repeat):
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
        random_algorithm = Algorithm(game)
        t, m = random_algorithm.run_algorithm(export=False)
        tries.append(t)
        moves.append(m)
        
        if export and m == min(moves):
            game.export_solution(output_name=f"results/output{board}_random.csv")
   
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")


if __name__ == '__main__': 
    game = RushHour(6, "gameboards/Rushhour6x6_test.csv")
    game.start_game()