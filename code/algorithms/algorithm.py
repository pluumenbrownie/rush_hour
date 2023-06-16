import random as rd

from classes.models import RushHour as RushHour
from classes.vehicle import * 


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


    def find_blocking_vehicle(self, target_car: Car|Truck) -> Car|Truck:
        """
        Find the vehicles that are blocking the red car 
        """
        target_tiles = set(self.get_tiles_occupied())
        for vehicle in self.vehicles:
        if vehicle != self:
            occupied_tiles = set(self.get_tiles_occupied())
            if target_tiles.intersection(occupied_tiles):
                return vehicle
        return None


# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
