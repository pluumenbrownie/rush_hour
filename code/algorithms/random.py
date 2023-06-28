import random as rd

from classes.models import RushHour as RushHour
from algorithms.algorithm import Algorithm

class Random(Algorithm):
    """ 
    A class to use algorithms to solve the game. 
    """
            
    def optimize_random(self):
        """
        Optimizes the solution by removing unnecessary moves.
        Return the amount of moves. 
        """
        self.game.optimize_solution()
        return len(self.game.history)
    
    def run(self, export: bool = True) -> tuple[int, int]:
        """ 
        Solves the rushhour game by selecing random cars and moves. 
        """
        counter = 0
        success_counter = 0

        while not self.game.is_won():
            # Choose a random car and a random directon 
            vehicle = self.choose_vehicle() 
            move = self.choose_direction()

            # Move the car in the game
            success = self.game.process_turn(vehicle, move)
           
            # Add counter 
            counter += 1 
            if success:
                success_counter += 1
       
       # Print the output of the game in output.csv
        if export:
            self.game.export_solution()
       
        print(f"It took the algorithm {counter} tries, {success_counter} of which were valid.")
       
        return counter, success_counter