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
        
    def run_algorithm(self, export: bool = True):
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

    def choose_direction(self):
        """
        Choose vehicle to move by randomly selecting from list of available cars.
        """
        return rd.choice(self.directions)

    def choose_vehicle(self):
        """
        Choose move direction by randomly selecting from list of available directions.
        """
        return rd.choice(self.vehicle_ids)


# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
