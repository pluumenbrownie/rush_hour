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
        """
        Initalizes a greedy algorithm that uses an archive 
        """
        self.game = game
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = game.get_vehicle_ids()
        self.directions = [1, -1]
        self.archive = set()
        self.moves: int = 0
    
    def move_red_car(self) -> bool: 
        """
        Moves the red car if that's possible 
        """
        success = self.game.process_turn("X", 1)
        if not success:
            return False
        
        # Check if state is already in archive
        visited = self.game.get_board_hash()

        # If state has not been visited, add it to archive 
        if visited not in self.archive:
            self.archive.add(visited)
            self.moves += 1
            return True 
        
        # If state is already in archive, undo move
        self.game.process_undo()
        return False 
    
    def move_blocking_vehicle(self) -> bool: 
        """
        Moves a vehicle that is blocking the red car 
        """
        # Find the blocking vehicle using the red car as the target vehicle 
        red_car = self.vehicles["X"]
        blocking_vehicle = self.find_blocking_vehicle(red_car, 1) 

        if blocking_vehicle: 
            # Choose a random direction for vehicle 
            direction = self.choose_direction()
            success = self.game.process_turn(blocking_vehicle.id, direction)
            if not success:
                return False

            # Check if state is already in archive
            visited = self.game.get_board_hash() 

            # If state is a new state, add state to archive 
            if visited not in self.archive:
                self.moves += 1
                self.archive.add(visited)
                return True 

            self.game.process_undo()
            return False 

    
    def move_random_movable_car(self) -> bool: 
        """
        This is no longer used as I have chosen to randomly select a car, independent of whether it can move or not       
        If no other moves are possible, select a random car from the movable vehicles list
        """
        # Get a list of vehicles that can be moved  including the direction
        movable_vehicles = self.game.get_movable_vehicles()
        
        # Choose a random vehicle and direction 
        vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)

        # Check if move is possible. If so, return true
        success = self.game.process_turn(vehicle, direction)
        if success: 
            return True 
        
        return False
    
    def move_random_car(self) -> bool: 
        """
        If no other moves are possible, select a random car and a random direction 
        """
        # Select a random car and a random direction 
        vehicle = self.choose_vehicle()
        direction = self.choose_direction()

        # Make move. If it's succesful, return true 
        success = self.game.process_turn(vehicle, direction)
        if success:
            self.moves += 1
            return True
        
        return False

    def run(self, export: bool = True) -> tuple[int, int]:
        """
        Run the greedy algorithm. It returns the tries and moves (valid tries)
        """
        count_tries = 0

        # Loop through until the game is solved 
        while not self.game.is_won():
            count_tries += 1

            # try to move red car to the right
            if self.move_red_car(): 
                continue

            # try to move the vehicle that is blocking the red car
            if self.move_blocking_vehicle():
                continue
            
            # if the first two options weren't possible, move a random car 
            if self.move_random_car(): 
                continue
        
        if export:
            self.game.export_solution()

        print(f"It took the algorithm {count_tries} tries and {self.moves} moves")
        
        return count_tries, self.moves