import copy
import random as rd

# from algorithms.algorithm import Algorithm
from classes.models import RushHour as RushHour

class Greedy2():
    """ 
    This class assigns the best possible option to each car. 
    """

    def __init__(self, game: RushHour):
        self.game = game 
        self.vehicles = game.get_vehicles()

    def solve(self):
    # Uses the random algorithm and a heuristic to get a better algorithm

        # Loop through the game as long as the game isn't won
        counter = 0 
        while not self.game.is_won():  
            # Best move is to move the red car to the right
            # Check if the red car can move to the exit
            if self.can_red_move(): 
                success = self.process_turn('X', 1)
                counter += 1 
                break
            
            # Second best move is to move a car that is blocking the red car
            # Check if you can move a vehicle blocking the red car
            blocking_vehicles = self.find_blocking_vehicles()
            closest_blocking_vehicle = self.find_closest_blocking_vehicle(blocking_vehicles)
            if self.can_blocker_move(closest_blocking_vehicle): 
                success = self.process_turn(closest_blocking_vehicle, 1)
                counter += 1 
                break 
            
            # Third best move is to move a car that is blocking a car that is blocking the red car
            second_closest_blocking_vehicle = self.find_second_closest_blocking_vehicle(closest_blocking_vehicle)
            if self.can_blocker_move(second_closest_blocking_vehicle): 
                success = self.process_turn(second_closest_blocking_vehicle, 1)
                counter += 1 
                break 
              
            # Otherwise pick a random vehicle and a random move 
            else: 
                # choose a random vehicle
                vehicle = self.choose_vehicle() 
                # Choose a random move
                move = self.choose_direction()
                # move the vehicle in the game
                success = self.game.process_turn(vehicle, move)
                    
        # Print the output
        print(f"It took the algorithm {counter} tries")


    def can_red_move(self):
        """
        Checks whether red car can move towards the exit 
        """
        target_vehicle = "X"
        direction = 1 
        move_viability = self.game_board.is_move_valid(target_vehicle, direction)
        if move_viability: 
            return True

        return False 
    
    def can_blocker_move(self, blocker): 
        """
        Checks whether a vehicle that's blocking the red car can move 
        """
        return self.game.is_move_valid(blocker, 1) 

    def find_closest_blocking_vehicle(self):
        """
        Of all the vehicles that are blocking the red car, find the closest to the vehicle 
        """
        target_vehicle = "X"
        blocking_vehicles = self.find_blocking_vehicles(target_vehicle)

        closest_vehicle = None
        closest_distance = float('inf')

        target_vehicle_position = self.find_vehicle_position('R')
        for blocking_vehicle in blocking_vehicles:
            vehicle_position = self.find_vehicle_position(blocking_vehicle)
            distance = abs(vehicle_position[0] - target_vehicle_position[0]) + abs(vehicle_position[1] - target_vehicle_position[1])
            if distance < closest_distance:
                closest_vehicle = blocking_vehicle
                closest_distance = distance
        
        return closest_vehicle
    
    def find_second_closest_blocking_vehicle(self, closest_vehicle):
        red_car_position = self.find_car_position('R')
        
        second_closest_blocking_vehicle = None
        second_closest_distance = float('inf')
        
        for row, row_vals in enumerate(self.board):
            for col, val in enumerate(row_vals):
                if val != '-' and val != 'R' and val != closest_vehicle:
                    if row == red_car_position[0] and col > red_car_position[1]:
                        distance = col - red_car_position[1]
                        if distance < second_closest_distance:
                            second_closest_blocking_vehicle = val
                            second_closest_distance = distance
        
        return second_closest_blocking_vehicle
    
    def find_vehicle_position(self, vehicle):
        """
        Find the position of a vehicle 
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == vehicle:
                    return (row, col)
        
        return None


    def find_blocking_vehicles(self, target_car):
        """
        Find the vehicles that are blocking the red car 
        """
        blocking_vehicles = []
        target_car_position = self.find_vehicle_position(target_car)
        
        for row in range(len(self.game)):
            for col in range(len(self.game[row])):
                if self.game[row][col] != '-' and self.game[row][col] != target_car:
                    if row == target_car_position[0] and col > target_car_position[1]:
                        blocking_vehicles.append(self.board[row][col])
        
        print(f"Blocking vehicle: {blocking_vehicles}")
        return blocking_vehicles
    

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

if __name__ == '__main__': 
    board_file = "gameboards/Rushhour6x6_1.csv"
    game =  RushHour(6, board_file)
    solver = Greedy2(game)
    solver.solve()

    
