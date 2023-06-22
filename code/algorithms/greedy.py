import random as rd

from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour
from classes.vehicle import * 

class Greedy(Algorithm):
    """ 
    This class assigns the best possible option to each car. 
    It first checks if it can move the red car. 
    If that's not the case, it checks whether it can move the car that blocking the red car. 
    If that's not the case, it selects a random move. 
    """
    def __init__(self, game:RushHour) -> None: 
        self.game = game
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = game.get_vehicle_ids()
        self.directions = [1, -1]

        self.archive = set()

        # self.last_move: tuple[str, int] = 'A', 1
    
    def move_red_car(self) -> bool: 
        """
        Moves the red car if that's possible 
        If it moves, self.last_move is set to the new move 
        """
        self.game.process_turn("X", 1)
        visited = self.game.get_board_hash()

        if visited not in self.archive:
            self.archive.add(visited)
            # print("red move")
            # self.last_move = 'X', 1
            return True 
        
        self.game.process_undo()
        return False 
    
    def move_blocking_vehicle(self) -> bool: 
        """
        Moves a vehicle that is blocking the red car 
        """
        red_car = self.vehicles["X"]

        # find the blocking vehilce 
        blocking_vehicle = self.find_blocking_vehicle(red_car, 1) 
        print(f"blocking vehicle: {blocking_vehicle}")

        if blocking_vehicle: 
            # choose a random direction for vehicle 
            direction = self.choose_direction()
            self.game.process_turn(blocking_vehicle.id, direction)
            visited = self.game.get_board_hash() 

            if visited not in self.archive:
                self.archive.add(visited)
                return True 
        
            self.game.process_undo()
            return False 

    
    def move_random_car(self) -> bool: 
        # get a list of vehicles that can be moved  including the direction
        movable_vehicles = self.game.get_movable_vehicles()
        
        # choose a random vehicle and direction 
        vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)

        self.game.process_turn(vehicle, direction)
        visited = self.game.get_board_hash() 

        if visited not in self.archive:
            self.archive.add(visited)
            return True 
    
        self.game.process_undo()
        return False 
    
    # def check_last_move(self, vehicle: str, direction: int) -> bool:
    #     if self.last_move[0] == vehicle and self.last_move[1] == direction * -1: 
    #         return False
    #     else:
    #         return True 

    def run(self) -> int:
        counter = 0

        while not self.game.is_won():
        # while counter <= 40:
            print("")
            self.game.show_board()
            counter += 1

            # try to move red car to the right
            if self.move_red_car(): 
                continue

            # try to move the vehicle that is blocking the red car
            if self.move_blocking_vehicle(): 
                continue
            
            # last option is to move a random car
            if self.move_random_car(): 
                continue

        print(f"It took the algorithm {counter} tries")
        return counter
