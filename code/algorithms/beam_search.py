import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst

class BeamSearch(BreadthFirst):
    """ 
    This class gives implements a beam search algorithm
    """

    def __init__(self, game:RushHour, beam_size: int):
        """ 
        Initializes an algorithm with the rushhour game.
        """
        self.game = copy.deepcopy(game)
        # Make a queue with a begin state
        self.queue = [copy.deepcopy(self.game)]
        self.visited_states = set()
        self.beam_size = beam_size



