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

        self.count_moves: int = 0

    
    def move_red_car(self) -> bool: 
        """
        Moves the red car if that's possible 
        If it moves, self.last_move is set to the new move 
        """
        success = self.game.process_turn("X", 1)
        if not success:
            return False
        
        visited = self.game.get_board_hash()

        if visited not in self.archive:
            self.archive.add(visited)
            self.count_moves += 1
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
        # print(f"blocking vehicle: {blocking_vehicle}")

        if blocking_vehicle: 
            # choose a random direction for vehicle 
            direction = self.choose_direction()
            success = self.game.process_turn(blocking_vehicle.id, direction)
            if not success:
                return False

            visited = self.game.get_board_hash() 

            if visited not in self.archive:
                self.count_moves += 1
                self.archive.add(visited)
                return True 
        
            self.game.process_undo()
            return False 

    
    def move_random_movable_car(self) -> bool: 
        # get a list of vehicles that can be moved  including the direction
        movable_vehicles = self.game.get_movable_vehicles()
        
        # choose a random vehicle and direction 
        vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)

        success = self.game.process_turn(vehicle, direction)
        if success: 
            # self.count_moves += 1
            return True 
        
        return False
    
    def move_random_car(self) -> bool: 
        # get a random car
        vehicle = self.choose_vehicle()

        # get a random direction
        direction = self.choose_direction()

        # make move 
        success = self.game.process_turn(vehicle, direction)

        if success:
            self.count_moves += 1
            return True
        
        return False


    def run(self) -> tuple[int, int]:
        count_tries = 0

        while not self.game.is_won():

            # print("")
            # self.game.show_board()
            count_tries += 1

            # try to move red car to the right
            if self.move_red_car(): 
                continue

            # try to move the vehicle that is blocking the red car
            if self.move_blocking_vehicle():
                continue
            
            # last option is to move a random movable car
            # if self.move_random_movable_car(): 
            #     # count_moves += 1
            #     continue

            if self.move_random_car(): 
                continue

        print(f"It took the algorithm {count_tries} tries and {self.count_moves} moves")
        return count_tries, self.count_moves
