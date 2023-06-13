from typing import Any
from classes.vehicle import *

import math as mt
import csv 
import pickle

class Move():
    """ 
    A move performed by a car. 
    """
    
    def __init__(self, target_id: str, direction: tuple[str, int]) -> None:
        """ 
        Initialize a move with the target vehicle ID and direction. 
        """
        self.target_id = target_id
        self.direction = direction

class RushHour():
    """ 
    A class for the game rush hour. 
    """
    
    def __init__(self, width: int, board_file: str) -> None:
        """ 
        Initialize the Rush Hour game with a board width and a board file.
        """
        self.game_board = Board(width)
        with open(board_file, 'r') as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = True
            for line in csv_reader: 
                if header:
                    header = False
                    continue
                veh_id = line[0].strip()
                orientation = line[1]
                col = int(line[2])
                row = int(line[3])
                length = int(line[4])
                # print(id, orientation, col, row, length)
                if length == 2:
                    new_vehicle = Car(veh_id, orientation, col, row)
                elif length == 3:
                    new_vehicle = Truck(veh_id, orientation, col, row)
                else:
                    raise ValueError("Vehicle can only be length 2 or 3.")
                self.game_board.add_vehicle(new_vehicle)
                
        self.game_board.print_board()
        self.history: list[tuple[str, int]] = []
        self.hash_set: set[int] = set()
    
    def show_board(self) -> None:
        """ 
        Print the current state of the game board.
        """
        self.game_board.print_board()
    
    def move_vehicle(self, vehicle_id: str, direction: int) -> bool:
        """ 
        Move a vehicle in the specified direction and return whether the move was successful.
        """
        move_viability = self.game_board.is_move_valid(vehicle_id, direction)
        #print("Can move:", move_viability)
        if move_viability:
            self.game_board.move_vehicle(vehicle_id, direction)
            self.hash_set.add(self.get_board_hash())
            return True
        return False
    
    def is_won(self) -> bool:
        """ 
        Check if the game is won. 
        """
        return self.game_board.is_won()
    
    def get_vehicles(self) -> dict[str, Car|Truck]:
        """ 
        Returns a dict with the Vehicle object in the game. 
        """
        return self.game_board.vehicle_dict

    def start_game(self) -> None:
        """ 
        Start the Rush Hour game and play until the game is won. 
        """
        turns = 0
        while not self.is_won():
            turns += 1
            # get user input
            print(f"Board hash: {self.get_board_hash()}")
            target_vehicle = input("What vehicle to move? ")
            direction = int(input("What direction? "))

            # process turn and show board
            success = self.process_turn(target_vehicle, direction)
            if not success:
                print("Move failed.")
            self.show_board()

        self.export_solution()
        print(f"You won! I'm so proud of you! (Took {turns} turns)")
    
    def process_turn(self, target_vehicle: str, direction) -> bool:
        """ 
        Try to move a target vehicle in a direction. 
        """
        try:
            success = self.move_vehicle(target_vehicle, direction)
        except ValueError as verror:
            print(verror)
            success = False
        except KeyError:
            print("Vehicle not found.")
            success = False

        if success:
            self.history.append((target_vehicle, direction))
        return success

    def export_solution(self, output_name: str = "results/output.csv"):
        """ 
        Export the solution history to a CSV file. 
        """
        with open(output_name, 'w') as file:
            file.write("car,move\n")
            for id, direction in self.history:
                file.write(f"{id},{direction}\n")
    
    def get_board_hash(self) -> int:
        return self.game_board.pickle_hash()


class Board():
    """ 
    Creates a board to which cars and trucks can be added.
    """

    def __init__(self, width: int) -> None:
        """ 
        Creates a empty board object with a width (6x6, 9x9, 12x12) and an exit. 
        """
        self.width = width

        self.board = []
        for _ in range(width):
            empty_row = []
            for _ in range(width):
                empty_row.append(None)
            self.board.append(empty_row)

        self.vehicle_dict: dict[str, Car|Truck] = {}
    
    def print_board(self) -> None:
        """ 
        Prints the board. 
        """
        for row in self.board:
            print(row)
    
    def add_vehicle(self, vehicle: Car|Truck) -> None:
        """ 
        Add a vehicle to the game board. 
        """
        coordinates_to_add = vehicle.get_tiles_occupied()
        for col, row in coordinates_to_add:
            self.board[row - 1][col - 1] = vehicle
        self.vehicle_dict[vehicle.id] = vehicle
    
    def is_move_valid(self, vehicle_id: str, direction: int) -> bool:
        """
        Check if a move is valid for a given vehicle and direction.

        ### Input
        - `vehicle_id: str`: String representing car to move.
        - `direction: int`:  -1 to move up/left, 1 to move down/right (movement
        depents on car orientation).  

        ### Output
        Returns False if move:
        - moves vehicle outside of the gameboard.
        - collides vehicle with another vehicle.

        Raises ValueError if direction is not 1 or -1.
        Raises KeyError if vehicle with `id=vehicle_id` does not exist.

        Returns True otherwise.
        """
        target_vehicle = self.vehicle_dict[vehicle_id]
        if not (direction == 1 or direction == -1):
            raise ValueError("Invalid move direction.")

        if target_vehicle.orientation == "H":

            # move to the left <-
            if direction == -1:
                if target_vehicle.col - 2 < 0:
                    return False
                next_tile = self.board[target_vehicle.row - 1][target_vehicle.col - 2]

            # move to the right ->
            elif direction == 1:
                if target_vehicle.col + target_vehicle.size > self.width:
                    return False
                next_tile = self.board[target_vehicle.row - 1][target_vehicle.col + target_vehicle.size - 1]

        elif target_vehicle.orientation == "V":

            # move up ^
            if direction == -1:
                if target_vehicle.row - 2 < 0:
                    return False
                next_tile = self.board[target_vehicle.row - 2][target_vehicle.col - 1]

            # move down v
            elif direction == 1:
                if target_vehicle.row + target_vehicle.size > self.width:
                    return False
                next_tile = self.board[target_vehicle.row + target_vehicle.size - 1][target_vehicle.col - 1]
            
        else:
            raise ValueError("Invalid direction in vehicle.")
        # print(next_tile)

        # return true if next_tile empty
        if next_tile:
            return False
        return True
    
    def move_vehicle(self, vehicle_id: str, direction: int) -> None:
        """ 
        Move a vehicle in the specified direction. 
        """
        target_vehicle = self.vehicle_dict[vehicle_id]

        # remove the vehicle
        tiles_to_empty = target_vehicle.get_tiles_occupied()
        for col, row in tiles_to_empty:
            self.board[row - 1][col - 1] = None

        # replace vehicle in new position
        target_vehicle.move(direction)
        tiles_to_fill = target_vehicle.get_tiles_occupied()
        for col, row in tiles_to_fill:
            self.board[row - 1][col - 1] = target_vehicle
    
    def is_won(self) -> bool:
        """ 
        Check if the game is won by checking the position of the red car. 
        """
        red_car = self.vehicle_dict["X"]
        if red_car.col == self.width - 1:
            return True
        return False

    def pickle_hash(self) -> int:
        return hash(pickle.dumps(self.vehicle_dict))
    

def count_statespace(width: int, board_file: str) -> int:
    """
    Determines statespace of a given Rush Hour gameboard.

    The game board is split in two games, containing either horizontally or 
    vertically aligned vehicles. Then, the amount of horizontally aligned vehicles 
    per row and vertically aligned vehicles per column are counted. The amount of
    free spaces per row/column is also tracked. Then the amount of states per row 
    is calculated via

    `states = n!/(v!(n-v)!)` with
    - `v` : #vehicles per row/column
    - `n` : #vehicles + #free_spaces
    
    The rows are then multiplied together and returned.
    """
    # H_cars will contain amount of horizontal vehicles per row
    H_cars = [0 for _ in range(width)]
    # amount of empty spaces per row
    H_spaces = [width for _ in range(width)]
    # V_cars will contain amount of vertical vehicles per column
    V_cars = [0 for _ in range(width)]
    # amount of empty spaces per column
    V_spaces = [width for _ in range(width)]

    with open(board_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = True
        for line in csv_reader: 
            # Skip the header
            if header:
                header = False
                continue
            # Horizontal vehicle
            if line[1] == "H":
                vehicle_row = int(line[3]) - 1
                H_cars[vehicle_row] += 1
                # Length of vehicle removes int(line[4]) empty spaces
                H_spaces[vehicle_row] -= int(line[4])
            # Vertical vehicle
            elif line[1] == "V":
                vehicle_col = int(line[2]) - 1
                V_cars[vehicle_col] += 1
                # Length of vehicle removes int(line[4]) empty spaces
                V_spaces[vehicle_col] -= int(line[4])

    states = 1
    # using i should be fine here
    for i in range(6):
        v = H_cars[i] 
        n = H_cars[i] + H_spaces[i]
        states *= (mt.factorial(n))//(mt.factorial(v)*mt.factorial(n - v))

        v = V_cars[i] 
        n = V_cars[i] + V_spaces[i]
        states *= (mt.factorial(n))//(mt.factorial(v)*mt.factorial(n - v))
    
    return states


if __name__ == '__main__': 
    board_file = "gameboards/Rushhour12x12_7.csv"
    print("State space size:", count_statespace(12, board_file))
    game = RushHour(12, board_file)
    # game.move_vehicle('AB', -1)
    game.start_game()