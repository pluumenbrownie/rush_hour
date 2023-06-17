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
    def run(self):
        counter = 0

        while not self.game.is_won():
            counter += 1
            # try to move red car to the right
            red_move = self.game.process_turn("X", 1)

            if not red_move:
                red_car = self.vehicles["X"]
    
                blocking_vehicle = self.find_blocking_vehicle(red_car, 1)

                if blocking_vehicle: 
                    direction = self.choose_direction()
                    blocking_vehicle_move = self.game.process_turn(blocking_vehicle.id, direction)
                    
                    if not blocking_vehicle_move:
                        break
            else: 
                # choose a random car
                vehicle = self.choose_vehicle() 
                # Choose a random direction
                direction = self.choose_direction()
                # move the car in the game
                random_move = self.game.process_turn(vehicle, direction)
    
  
        print(f"It took the algorithm {counter} tries")
        return counter

