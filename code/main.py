from algorithms.algorithm import Algorithm
from classes.models import RushHour

game = RushHour(6, "gameboards/Rushhour6x6_1.csv")
random_algorithm = Algorithm(game)
random_algorithm.random_algorithm()
