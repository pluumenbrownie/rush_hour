from classes.graphs import *
from algorithms.algorithm import Algorithm
from code.classes.models import RushHour as RushHour


class Dijkstra(Algorithm):
    """
    Builds a graph from a RushHour 
    """
    def __init__(self, game: RushHour) -> None:
        super().__init__(game)
