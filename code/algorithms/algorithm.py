import random as rd

from classes.models import RushHour as RushHour


class Algorithm():
    """ 
    A class to use algorithms to solve the game. 
    """
    
    def __init__(self, game: RushHour) -> None:
        """ 
        Initializes an algorithm with target vehicle id, directions and the rushhour game. 
        """
        self.game = game
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = game.get_vehicle_ids()
        self.directions = [1, -1]
        
    def choose_direction(self) -> int:
        """
        Choose vehicle to move by randomly selecting from list of available cars.
        """
        return rd.choice(self.directions)

    def choose_vehicle(self) -> str:
        """
        Choose move direction by randomly selecting from list of available directions.
        """
        return rd.choice(self.vehicle_ids)


# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
