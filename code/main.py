from algorithms.algorithm import Algorithm
from classes.models import RushHour
import time
import statistics as stat

if __name__ == '__main__': 
    
    start_time = time.time()

    tries: list[int] = []
    moves: list[int] = []
    repeat = 100
    for _ in range(repeat):
        game = RushHour(12, "gameboards/Rushhour12x12_7.csv")
        random_algorithm = Algorithm(game)
        t, m = random_algorithm.random_algorithm(export=False)
        tries.append(t)
        moves.append(m)
    
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time:.3f} seconds.")

    print(f"On average, in {repeat} games, took {round(stat.mean(tries))}±{round(stat.stdev(tries))} tries and {round(stat.mean(moves))}±{round(stat.stdev(moves))} succesfull moves.")
    

    