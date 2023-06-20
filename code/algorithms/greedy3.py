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
        last_move: tuple[str, int] = 'A', 1

        while not self.game.is_won():\
        # while counter <= 20:
            # self.game.show_board()
            print("\n")

            counter += 1
            # to prevent ending up in a loop
 

            # try to move red car to the right
            red_move = self.game.process_turn("X", 1)

            # if red can move, continue to another round of the loop
            if red_move:
                continue 

            # look to right of the red car to see which vehicle is blocking
            red_car = self.vehicles["X"]
            blocking_vehicle = self.find_blocking_vehicle(red_car, 1) 
            print(f"blocking vehicle: {blocking_vehicle}")

            # try to move the vehicle that is blocking the red car
            if blocking_vehicle: 
                # choose a random direction
                direction = self.choose_direction()
                # check if we are not undoing the last move and end up in a loop
                if last_move[0] == blocking_vehicle.id and last_move[1] == direction * -1: 
                    continue
                
                # make move
                blocking_vehicle_move = self.game.process_turn(blocking_vehicle.id, direction)

                if blocking_vehicle_move:
                    print("blocking vehicle was moved")
                    last_move = blocking_vehicle.id, direction
                    continue
                
                if not blocking_vehicle_move: 
                    direction = direction * -1 
                    # check if we're not undoing the last move
                    if last_move[0] == blocking_vehicle.id and last_move[1] == direction * -1: 
                        movable_vehicles = self.game.get_movable_vehicles()
                        vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)
                        random_move = self.game.process_turn(vehicle, direction)
                        print("random move")
                        continue
                    # make move 
                    blocking_vehicle_move = self.game.process_turn(blocking_vehicle.id, direction)
                    last_move = blocking_vehicle.id, direction

            # if no other move was possible, make a random move 
            movable_vehicles = self.game.get_movable_vehicles()
            vehicle, direction = self.choose_vehicle_from_movable_vehicles(movable_vehicles)
            print(vehicle, direction)
            if last_move[0] == vehicle and last_move[1] == direction * -1: 
                continue
            random_move = self.game.process_turn(vehicle, direction)
            if random_move: 
                last_move = vehicle, direction
                print("random move")

            print(counter)

        print(f"It took the algorithm {counter} tries")
        return counter
