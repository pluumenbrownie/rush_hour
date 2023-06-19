import random as rd

from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour
from classes.vehicle import * 

class Greedy3(Algorithm):
    """ 
    This class assigns the best possible option to each car. 
    It first checks if it can move the red car. 
    If that's not the case, it checks whether it can move the car that blocking the red car. 
    If that's not the case, it selects a random move. 
    """
    def run(self) -> int:
        counter = 0

        while not self.game.is_won():
            self.game.show_board()
            print("\n")
            counter += 1

            # try to move red car to the right
            red_move = self.game.process_turn("X", 1)

            if red_move:
                continue 

            red_car = self.vehicles["X"]
            # look to right of the red car to see which vehicle is blocking
            blocking_vehicle = self.find_blocking_vehicle(red_car, 1) 
            # try to move the vehicle that is blocking the red car
            if blocking_vehicle: 
                direction = self.choose_direction()
                blocking_vehicle_move = self.game.process_turn(blocking_vehicle.id, direction)
                
                if not blocking_vehicle: 
                    direction = direction * -1 
                    blocking_vehicle_move = self.game.process_turn(blocking_vehicle.id, direction)

                if blocking_vehicle_move:
                    # print("blocking vehicle was moved")
                    continue

            if blocking_vehicle: 
                second_blocking_vehicle = self.find_blocking_vehicle(blocking_vehicle, 1) 




            
            # if no other move was possible, make a random move 
            movable_vehicles = self.game.get_movable_vehicles()
            vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)
            random_move = self.game.process_turn(vehicle, direction)
            if random_move: 
                print("random move")

            # # choose a random car
            # vehicle = self.choose_vehicle() 
            # # choose a random direction
            # direction = self.choose_direction()
            # move the car in the game
            # random_move = self.game.process_turn(vehicle, direction)
            # if random_move: 
            #     print("random vehicle was moved")

            print(counter)

        print(f"It took the algorithm {counter} tries")
        return counter
