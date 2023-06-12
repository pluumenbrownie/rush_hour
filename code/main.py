from algorithms.algorithm import Algorithm
from classes.models import RushHour
import time

if __name__ == '__main__': 
    
    start_time = time.time()
    
    game = RushHour(6, "gameboards/Rushhour6x6_1.csv")
    random_algorithm = Algorithm(game)
    random_algorithm.random_algorithm()
    
    end_time = time.time()
    print(f"The random algorithm took {end_time - start_time} seconds.")
    

    