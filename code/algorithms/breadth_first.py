import copy

from classes.models import RushHour
from algorithms.depth_first import DepthFirst

class BreadthFirst(DepthFirst):
    """ 
    This class gives implements a breadth first algorithm
    FIFO: first in, first out
    """
            
    def get_next_state(self) -> RushHour:
        """
        Method that get the first state from the list of states.
        Now the stack works like a queue
        """
        return self.stack.pop(0)