import copy
import random as rd

from algorithms.algorithm import Algorithm as Algorithm
from classes.models import RushHour as RushHour

class Greedy():
    """ This class assigns the best possible option to each car. """
    def __init__(self, game: RushHour):
        """ 
        Initializes an algorithm with target vehicle id, directions and the rushhour game. 
        """
        self.game = game
    # Uses the random algorithm and a heuristic to get a better algorithm
    # Loop through the game as long as the game isn't won
    # Check if the red car can move to the exit
    # Check if you can move a car blocking the red car
    
    # Otherwise pick a random car and a random move 
    # Print the output
    
    def greedy_algorithm(self, algorithm):
        """
        Method to test a greedy algorithm. 
        """
        red_car = self.pos_red_car
        while not self.game.is_won():
            # Check if the red car can move to the exit
            # Check if you can move a car blocking the red car
            # Pick a random car and a random move
            vehicle = algorithm.choose_vehicle()
            move = algorithm.choose_direction()
            success = self.game.process_turn(vehicle, move)
        # Print the output of the game in output.cs
        self.game.export_solution()
            
# --------------------------------------------------------------------------------------------------------#
    # Heuristics:
    # Best move is to move the red car to the right
    def pos_red_car(self, algorithm):
        """ 
        This method returns the position of the red car. 
        """
        for car in algorithm.vehicle_ids:
            if car.vehicle_ids == 'X':
                return car
        
    # Second best move is to move a car that is blocking the red car
    # Third best move is to move a car that is blocking a car that is blocking the red car
    
    # add an archive -> put a state in a set 
    # -> state of the board serializing into a tuple.. (Use to hash)
    # numpy overwegen 