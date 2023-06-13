import copy
import random as rd

from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour

class greedy_algorithm():
    """ This class assigns the best possible option to each car. """
    
    # Uses the random algorithm and a heuristic to get a better algorithm
    # Loop through the game as long as the game isn't won
    # Check if the red car can move to the exit
    # Check if you can move a car blocking the red car
    # Otherwise pick a random car and a random move 
    # Print the output
    
# --------------------------------------------------------------------------------------------------------#
    # Heuristics:
    # Best move is to move the red car to the right
    # Second best move is to move a car that is blocking the red car
    # Third best move is to move a car that is blocking a car that is blocking the red car
    
    # add an archive -> put a state in a set 
    # -> state of the board serializing into a tuple.. (Use to hash)
    # numpy overwegen 