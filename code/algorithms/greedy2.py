import random as rd

# from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour

class Greedy2():
    """ 
    This class assigns the best possible option to each car. 
    Greedy2 only looks if the red car can move and if not, chooses a random car
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
        random_moves = 0 
        
        while not self.game.is_won():  
            # Best move is to move the red car to the right
            # Check if the red car can move to the exit and if so, move the red car to the exit 
            success = self.game.process_turn(red_car, 1)
            if success: 
                counter += 1 
                first_choice_moves += 1
                          
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
        print(f"Random moves: {random_moves}.")    


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