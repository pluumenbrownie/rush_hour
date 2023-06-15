import random as rd

# from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour

class Greedy3():
    """ 
    This class assigns the best possible option to each car. 
    It first checks if it can move the red car. 
    If that's not the case, it checks whether it can move the car that blocking the red car. 
    If that's not the case, it checks what vehicle is blocking the blocking car. 
    If that's not the case, it selects a random move. 
    """

    def __init__(self, game: RushHour):
        self.game = game 
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = [id for id in self.vehicles.keys()]
        self.directions = [1, -1]

    def solve(self):
    # Uses the greedy algorithm and a heuristic to get a better algorithm

        # Loop through the game as long as the game isn't won
        red_car = "X"
        counter = 0 
        first_choice_moves = 0
        second_choice_moves = 0 
        third_choice_moves = 0
        random_moves = 0 
        
        while not self.game.is_won():  
            # Best move is to move the red car to the right
            # Check if the red car can move to the exit and if so, move the red car to the exit 
            success = self.game.process_turn('X', 1)
            if success: 
                counter += 1 
                first_choice_moves += 1
            
            # Second best move is to move a vehicle that is blocking the red car
            # Check if you can move a vehicle blocking the red car and if so, move the vehicle 
            closest_blocking_vehicle = self.find_blocking_vehicles(red_car)
            # For now, it's a random direction 
            direction = self.choose_direction()
            success2 = self.game.process_turn(closest_blocking_vehicle, direction)
            if success2:  
                counter += 1  
                second_choice_moves += 1 
            
            # Third best move is to move a car that is blocking a car that is blocking the red car
            second_closest_blocking_vehicle = self.find_blocking_vehicles(closest_blocking_vehicle)
            
            # For now, it's a random direction 
            direction = self.choose_direction()
            success3 = self.game.process_turn(second_closest_blocking_vehicle, direction)
            if success3:
                counter += 1 
                third_choice_moves += 1
                          
            # Otherwise pick a random vehicle and a random move 
            else: 
                # choose a random vehicle
                vehicle = self.choose_vehicle() 
                # Choose a random move
                move = self.choose_direction()
                # move the vehicle in the game
                success4 = self.game.process_turn(vehicle, move)
                if success4: 
                    counter += 1 
                    random_moves += 1

                    
        # Print the output
        print(f"It took the algorithm {counter} tries.")
        print(f"First choice moves: {first_choice_moves}.")
        print(f"Second choice moves: {second_choice_moves}.")
        print(f"Third choice moves: {third_choice_moves}.")
        print(f"Random moves: {random_moves}.")    
    
    def find_vehicle_position(self, vehicle):
        """
        Find the position of a vehicle 
        """
        for row in range(self.game.game_board.width):
            for col in range(self.game.game_board.width):
                if self.game.game_board.board[row][col] == vehicle:
                    return (row, col)
        
        return None
    

    def find_blocking_vehicles(self, target_car):
        """
        Find the vehicles that are blocking the red car 
        """
        blocking_vehicles = []
        target_car_position = self.find_vehicle_position(target_car)

        if target_car_position is None:
            return blocking_vehicles
        
        for row in range(self.game.game_board.width):
            for col in range(self.game.game_board.width):
                if self.game.game_board.board[row][col] is not None and self.game.game_board.board[row][col] != target_car:
                    if row == target_car_position[0] and col > target_car_position[1]:
                        print(f"Before: {blocking_vehicles}")
                        blocking_vehicles.append(self.game.game_board[row][col])
                        print(f"After: {blocking_vehicles}")

        
        print(f"Blocking vehicle: {blocking_vehicles}")
        # Only return the first vehicle in the list 
        return blocking_vehicles[0]


    def choose_direction(self):
        """
        Choose vehicle to move by randomly selecting from list of available cars.
        This method was copied from random algorithm 
        """
        return rd.choice(self.directions)

    def choose_vehicle(self):
        """
        Choose move direction by randomly selecting from list of available directions.
        This method was copied from random algorithm 
        """
        return rd.choice(self.vehicle_ids)

# --------------------------------------------------------------------------------------------------------#
    # Heuristics:
    # Best move is to move the red car to the right
    # Second best move is to move a car that is blocking the red car
    # Third best move is to move a car that is blocking a car that is blocking the red car
    
    # add an archive -> put a state in a set 
    # -> state of the board serializing into a tuple.. (Use to hash)
    # numpy overwegen 

