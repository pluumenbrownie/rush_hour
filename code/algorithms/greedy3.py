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

    def solve(self) -> tuple[int, int, int, int, int]: 
    # Uses the greedy algorithm and a heuristic to get a better algorithm

        # Loop through the game as long as the game isn't won
        red_car = self.vehicles['X']
        counter = 0 
        first_choice_moves = 0
        second_choice_moves = 0 
        third_choice_moves = 0
        random_moves = 0 
        
        while not self.game.is_won():  
            # Best move is to move the red car to the right
            # Check if the red car can move to the exit and if so, move the red car to the exit 
            move = self.game.process_turn('X', 1)
            if move: 
                counter += 1 
                first_choice_moves += 1
            
            # Second best move is to move a vehicle that is blocking the red car
            # Check if you can move a vehicle blocking the red car and if so, move the vehicle 
           
            # For now, for horizontal vehicles we look at cars at their left
            # For vertical vehicles we look at vehicles below them 
            direction = 1 
            closest_blocking_vehicle = self.find_blocking_vehicle(red_car, direction)

            # Check if you can move this vehicle
            move2 = False 
            if closest_blocking_vehicle and move == False: 
                success2 = self.game.process_turn(closest_blocking_vehicle.id, 1)
                if success2: 
                    counter += 1  
                    second_choice_moves += 1 
                    move2 = True
                else: 
                    success2 = self.game.process_turn(closest_blocking_vehicle.id, -1)
                    if success2: 
                        counter += 1  
                        second_choice_moves += 1 
                        move2 = True
    
            # Third best move is to move a car that is blocking a car that is blocking the red car
            if move2 == False: 
                second_closest_blocking_vehicle = self.find_blocking_vehicle(closest_blocking_vehicle, direction)
                if second_closest_blocking_vehicle: 
                    success3 = self.game.process_turn(second_closest_blocking_vehicle.id, 1)
                    if success3: 
                        counter += 1  
                        third_choice_moves += 1 
                    else: 
                        success3 = self.game.process_turn(second_closest_blocking_vehicle.id, -1)
                        if success3: 
                            counter += 1  
                            third_choice_moves += 1 
                
            # Otherwise pick a random vehicle and a random move 
            else:
                # choose a random vehicle
                vehicle = self.choose_vehicle() 
                # Choose a random move
                direction = self.choose_direction()
                # move the vehicle in the game
                move4 = self.game.process_turn(vehicle, move)
                if move4: 
                    counter += 1 
                    random_moves += 1

                    
        # Print the output
        print(f"It took the algorithm {counter} tries.")
        print(f"First choice moves: {first_choice_moves}.")
        print(f"Second choice moves: {second_choice_moves}.")
        print(f"Third choice moves: {third_choice_moves}.")
        print(f"Random moves: {random_moves}.")

        return counter, first_choice_moves, second_choice_moves, third_choice_moves, random_moves


# --------------------------------------------------------------------------------------------------------#
    # Heuristics:
    # Best move is to move the red car to the right
    # Second best move is to move a car that is blocking the red car
    # Third best move is to move a car that is blocking a car that is blocking the red car
    
    # add an archive -> put a state in a set 
    # -> state of the board serializing into a tuple.. (Use to hash)
    # numpy overwegen 

