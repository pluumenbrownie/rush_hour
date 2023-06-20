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
    
    def choose_vehicle_from_movable_vehicles(self, movable_vehicles: list[tuple[str, int]]) -> tuple[str, int]:
        """
        Choose move direction by randomly selecting from list of available directions.
        """
        return rd.choice(movable_vehicles)


    def find_blocking_vehicle(self, target_car: Car|Truck, direction: int) -> Car|Truck|None:
        """
        Find the vehicles that are blocking the red car 
        Pre: get red car
        Post: get blocking car 
        """
        # Get position of target car
        vehicle = self.vehicles[target_car.id]
        row = vehicle.row
        col = vehicle.col
        # print(f"row of target car: {row}, column of target car: {col}")
        orientation = vehicle.orientation

        # If the car is horizontal, look at the row + 1 
        if orientation == "H": 
             # Get the car who's blocking the red car 
            if direction == 1:
                blocking_vehicle = self.game.get_vehicle_from_location(col + 1 + (vehicle.size - 1), row)
            else: 
                blocking_vehicle = self.game.get_vehicle_from_location(col - 1, row)
        else: 
            # Get the car who's blocking the red car 
            if direction == 1:
                blocking_vehicle = self.game.get_vehicle_from_location(col, row + 1 + (vehicle.size -1))
            else: 
                blocking_vehicle = self.game.get_vehicle_from_location(col, row - 1)

        return blocking_vehicle
        

# if __name__ == '__main__': 
#     board_file = "gameboards/Rushhour6x6_1.csv"
#     game =  RushHour(6, board_file)
#     solver = Algorithm(game)
#     solver.random_algorithm()

    
