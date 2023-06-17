import random as rd

from classes.models import RushHour as RushHour
from algorithms.algorithm import Algorithm



class Random(Algorithm):
    """ 
    A class to use algorithms to solve the game. 
    """
            
    def run(self, export: bool = True) -> tuple[int, int]:
        """ 
        Solves the rushhour game by selecing random cars and moves. 
        """
        counter = 0
        success_counter = 0
        while not self.game.is_won():
            # choose a random car
            vehicle = self.choose_vehicle() 
            # Choose a random move
            move = self.choose_direction()
            # move the car in the game
            success = self.game.process_turn(vehicle, move)
            # add counter 
            counter += 1 
            if success:
                success_counter += 1
        # Print the output of the game in output.csv
        if export:
            self.game.export_solution()
        print(f"It took the algorithm {counter} tries, {success_counter} of which were valid.")
        return counter, success_counter


# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
