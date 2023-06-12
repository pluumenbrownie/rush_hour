import random as rd

from classes.models import RushHour as RushHour


class Algorithm():
    """ 
    A class to use algorithms to solve the game. 
    """
    
    def __init__(self, game: RushHour):
        """ 
        Initializes an algorithm with target vehicle id, directions and the rushhour game. 
        """
        self.game = game
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = [id for id in self.vehicles.keys()]
        self.directions = [1, -1]
        
    def random_algorithm(self):
        """ 
        Solves the rushhour game by selecing random cars and moves. 
        """
        counter = 0
        success_counter = 0
        while not self.game.is_won():
            # Choose a random move
            move = rd.choice(self.directions)
            # choose a random car
            vehicle = rd.choice(self.vehicle_ids) 
            # move the car in the game
            success = self.game.process_turn(vehicle, move)
            # add counter 
            counter += 1 
            if success:
                success_counter += 1
        # Print the output of the game in output.csv
        self.game.export_solution()
        print(f"It took the algorithm {counter} tries, {success_counter} of which were valid.")

# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
