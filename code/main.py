from algorithms.algorithm import Algorithm
from classes.models import RushHour
import time
import statistics as stat

if __name__ == '__main__': 
    
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    repeat = 1000
    for _ in range(repeat):
        game = RushHour(9, "gameboards/Rushhour9x9_4.csv")
        random_algorithm = Algorithm(game)
        t, m = random_algorithm.run_algorithm(export=False)
        tries.append(t)
        moves.append(m)
        if m == min(moves):
            game.export_solution(output_name="results/output9x9_4_random.csv")
    
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")
    

    