import random as rd

from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour
from classes.vehicle import * 

class Greedy3(Algorithm):
    """ 
    This class assigns the best possible option to each car. 
    It first checks if it can move the red car. 
    If that's not the case, it checks whether it can move the car that blocking the red car. 
    If that's not the case, it checks what vehicle is blocking the blocking car. 
    If that's not the case, it selects a random move. 
    """

    def run_algorithm(self) -> tuple[int, int, int, int, int]: 
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
            closest_blocking_vehicle = self.find_blocking_vehicle(red_car)
            move = self.game.game_board.is_move_valid(closest_blocking_vehicle[id], 1)
            if move == True: 
                success2 = self.game.process_turn(closest_blocking_vehicle, 1)
                counter += 1  
                second_choice_moves += 1 
            else: 
                success2 = self.game.process_turn(closest_blocking_vehicle, -1)
                counter += 1  
                second_choice_moves += 1 
            
            # Third best move is to move a car that is blocking a car that is blocking the red car
            if success2 is False: 
                second_closest_blocking_vehicle = self.find_blocking_vehicle(closest_blocking_vehicle)
                move1 = self.game.game_board.is_move_valid(second_closest_blocking_vehicle[id], 1)
                move2 = self.game.game_board.is_move_valid(second_closest_blocking_vehicle[id], -1)

                if move1: 
                    success3 = self.game.process_turn(closest_blocking_vehicle, 1)
                    counter += 1  
                    third_choice_moves += 1 
                elif move2: 
                    success3 = self.game.process_turn(closest_blocking_vehicle, -1)
                    counter += 1  
                    third_choice_moves += 1 
                else: 
                    success3 = False
                # Add something that success3 is otherwise False 
                          
            # Otherwise pick a random vehicle and a random move 
            if success3 is False: 
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

        return counter, first_choice_moves, second_choice_moves, third_choice_moves, random_moves
    

    def find_blocking_vehicle(self, target_car: Car|Truck) -> Car|Truck:
        """
        Find the vehicles that are blocking the red car 
        """
        for row in range(self.game.game_board.width):
            for col in range(self.game.game_board.width):
                if self.game.game_board.board[row][col] is not None and self.game.game_board.board[row][col] != target_car:
                    if row == target_car_position[0] and col > target_car_position[1]:
                        print(f"Before: {blocking_vehicle}")
                        blocking_vehicles.append(self.game.game_board[row][col])
                        print(f"After: {blocking_vehicle}")

        
        print(f"Blocking vehicle: {blocking_vehicle}")
        # Only return the first vehicle in the list 
        return blocking_vehicle 


# --------------------------------------------------------------------------------------------------------#
    # Heuristics:
    # Best move is to move the red car to the right
    # Second best move is to move a car that is blocking the red car
    # Third best move is to move a car that is blocking a car that is blocking the red car
    
    # add an archive -> put a state in a set 
    # -> state of the board serializing into a tuple.. (Use to hash)
    # numpy overwegen 

