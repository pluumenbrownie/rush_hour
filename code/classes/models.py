from typing import Type
from classes.vehicle import *

import math as mt
import csv 
import pickle


class RushHour():
    """ 
    A class for the game rush hour. 
    """
    
    def __init__(self, width: int, board_file: str) -> None:
        """ 
        Initialize the Rush Hour game with a board width and a board file.
        Pre: width of board and board file 
        Post: vehicles and board are created and vehicles are placed on the board 
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
        self.history: list[tuple[str, int, int]] = []
        self.hash_set: set[int] = set()
    
    def show_board(self) -> None:
        """ 
        Print the current state of the game board.
        Pre: nothing
        Post: board is printed 
        """
        self.game_board.print_board()
    
    def move_vehicle(self, vehicle_id: str, direction: int) -> bool:
        """ 
        Move a vehicle in the specified direction and return whether the move was successful.
        Checks if move of vehicle is valid, then moves the vehicle in de specified direction.
        ## Pre:
        - Vehicle corresponding to `vehicle_id` exists.

        Inputs:
        - vehicle_id: str - id of a vehicle (NOT of a car or truck class) 
        - direction: int - direction to move the vehicle. Can be `-1` or `1`
        
        ## Post: 
        - If move is possible:
            - Moves vehicle in the game.
            - Returns True
        - If move failed:
            - Returns False if move collides with vehicle or wall.
            - Raises ValueError if direction is not 1 or -1.
            - Raises KeyError if vehicle with `id=vehicle_id` does not exist.
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
        Pre: Vehicle with `id == "X"` exists.
        Post: returns True if game is won.
        """
        return self.game_board.is_won()
    
    def get_vehicles(self) -> dict[str, Car|Truck]:
        """ 
        Returns a dict with the Vehicle object in the game. 
        Pre: nothing
        Post: returns all vehicles as a dict 
        ## Example: 
        Game with `Car`s "A", "B" and "C" returns:
        ```
        {"A": Car A,
        "B": Car B,
        "C": Car C}
        ```
        """
        return self.game_board.vehicle_dict
    
    def get_vehicle_ids(self) -> list[str]:
        """
        Returns a list with the ids of all vehicles placed on the board.
        Pre: nothing
        Post: list of strings with the id's of vehicles placed on the board (not as objects)
        ## Example: 
        Game with `Car`s "A", "B" and "C" returns:
        ```
        ["A", "B", "C"]
        ```
        """
        return [id for id in self.game_board.vehicle_dict.keys()]
    
    def get_vehicle_from_location(self, row: int, col: int) -> None|Car|Truck:
        """
        Get the vehicle that's in a certain location
        Pre: a row and a column
        Post: you get an object (Car or Truck) or nothing 
        """
        return self.game_board.get_vehicle_from_location(row, col)

    def start_game(self) -> None:
        """ 
        Start the Rush Hour game and play until the game is won. 
        Pre: nothing
        During: user input is necessary
        Post: whether you won gets printed to the screen
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
    
    def process_turn(self, target_vehicle_id: str, direction: int) -> bool:
        """ 
        Try to move a target vehicle in a direction. Move is added to history if succesfull.
        Pre: id of a target verhicle (NOT an object) and a direction
        Post: if the move was succesful, it returns True and adds move to `self.history`.
        """
        try:
            success = self.move_vehicle(target_vehicle_id, direction)
        except ValueError as verror:
            print(verror)
            success = False
        except KeyError:
            print("Vehicle not found.")
            success = False

        if success:
            self.history.append((target_vehicle_id, direction, self.get_board_hash()))
        return success
    
    def get_movable_vehicles(self) -> list[tuple[str, int]]:
        """
        Returns list of all possible moves all vehicles in the current game state
        could make.
        - Pre: Game has vehicles.
        - Post: returns list of tuples, which contain the `vehicle.id` of the movable 
        vehicle and the direction of the move. 
        """
        # returns a dict with str and Vehicle object 
        vehicles = self.get_vehicles()
        # make empty list 
        movable_vehicles: list[tuple[str, int]] = []
        movable_vehicles_ids: list[str] = []
        
        # loop over all the vehicles on the board 
        for vehicle in vehicles: 
            if self.game_board.is_move_valid(vehicle, 1):
                # add tuple to list 
                movable_vehicles.append((vehicle, 1))


            if self.game_board.is_move_valid(vehicle, -1): 
                # add tuple to list 
                movable_vehicles.append((vehicle, -1))

        return movable_vehicles


    def export_solution(self, output_name: str = "results/output.csv") -> None:
        """ 
        Export the solution history to a CSV file. 
        ## Pre: 
        - Path to desired output location is valid.
        - Moves have been executed via `self.process_turn()` (as opposed to `self.move_vehicle()`)
        Input: 
        - output_name: str - Name of the file where you want to save the results.
            - Default = "results/output.csv"
        ## Post: 
        - File will be filled with all the moves. Existing file will be overwritten.
        """
        with open(output_name, 'w') as file:
            file.write("car,move\n")
            for id, direction, hash in self.history:
                file.write(f"{id},{direction}\n")
    
    def optimize_solution(self) -> None:
        """
        Try to remove unnecesairy moves from found solution with hashes.

        - Pre: The board is in a winning state
        - Post: `self.history` is replaced with an optimized, valid solution.
        """
        hash_seen: dict[int, int] = {}

        # count how often unique board_hashes exist in self.history
        for _, _, board_hash in self.history:
            if hash_seen.get(board_hash, False):
                hash_seen[board_hash] += 1
            else:
                hash_seen[board_hash] = 1
        
        new_history: list[tuple[str, int, int]] = []
        important_hash = None
        removed_steps = 0

        # build new history
        for veh_id, direction, board_hash in self.history:
            # print(f"{veh_id=}, {direction=}, {board_hash=}, {important_hash=}, {hash_seen[board_hash]=}" )
            # if we are not in a loop
            if not important_hash:
                new_history.append((veh_id, direction, board_hash))
            else:
                removed_steps += 1

            hash_seen[board_hash] -= 1
            # important_hash is set to the hash to indicate a loop
            if hash_seen[board_hash] > 0 and not important_hash:
                important_hash = board_hash
            elif hash_seen[board_hash] == 0 and important_hash == board_hash:
                important_hash = None
        
        percentage = round(removed_steps/len(self.history)*100, 1)
        print(f"Removed {removed_steps} steps ({percentage} %).")
        self.history = new_history
    
    def get_board_hash(self) -> int:
        """
        TO DO: Doc strings and pre and post should be added 
        Pre: 
        Post: 
        """
        return self.game_board.pickle_hash()

class Board():
    """ 
    Creates a board to which cars and trucks can be added.
    """

    def __init__(self, width: int) -> None:
        """ 
        Creates a empty board object with a width (6x6, 9x9, 12x12) and an exit. 
        Pre: width of board
        Post: empty board is created as a list 
        """
        self.width = width

        self.board: list[list[Car|Truck|None]] = []
        for _ in range(width):
            empty_row = []
            for _ in range(width):
                empty_row.append(None)
            self.board.append(empty_row)

        self.vehicle_dict: dict[str, Car|Truck] = {}
    
    def print_board(self) -> None:
        """ 
        Prints the board. 
        Pre: nothing
        Post: board gets printed to the screen
        """
        for row in self.board:
            print(row)
    
    def add_vehicle(self, vehicle: Car|Truck) -> None:
        """ 
        Add a vehicle object to the game board. 
        ## Pre: 
        - Location of added `Car` or `Truck` is unoccupied.

        Input:
        - vehicle: Car|Truck - object of vehicle that needs to be added to the board.
        ## Post: 
        - vehicle is added to the board.
        """
        coordinates_to_add = vehicle.get_tiles_occupied()
        for col, row in coordinates_to_add:
            self.board[row - 1][col - 1] = vehicle
        self.vehicle_dict[vehicle.id] = vehicle

    def get_vehicle_from_location(self, row: int, col: int) -> None|Car|Truck:
        """
        Get the vehicle that's in a certain location
        Pre: get the row and column 
        Post: it returns the object if there is one in the location, otherwise none 
        """
        return self.board[row-1][col-1]
    
    def is_move_valid(self, vehicle_id: str, direction: int) -> bool:
        """
        Check if a move is valid for a given vehicle and direction.

        ## Pre: 
        - `vehicle_id: str`: String representing car to move.
        - `direction: int`:  -1 to move up/left, 1 to move down/right (movement
        depents on car orientation).

        ## Post: 
        - Returns False if move:
            - moves vehicle outside of the gameboard.
            - collides vehicle with another vehicle.
        - Raises ValueError if direction is not 1 or -1.
        - Raises KeyError if vehicle with `id=vehicle_id` does not exist.
        - Returns True otherwise.
        """
        target_vehicle = self.vehicle_dict[vehicle_id]
        if not (direction == 1 or direction == -1):
            raise ValueError("Invalid move direction.")

        if target_vehicle.orientation == "H":

            # move to the left <-
            if direction == -1:
                if target_vehicle.col - 2 < 0:
                    return False
                next_tile = self.get_vehicle_from_location(target_vehicle.row, target_vehicle.col - 1)

            # move to the right ->
            elif direction == 1:
                if target_vehicle.col + target_vehicle.size > self.width:
                    return False
                next_tile = self.get_vehicle_from_location(target_vehicle.row, target_vehicle.col + target_vehicle.size)

        elif target_vehicle.orientation == "V":

            # move up ^
            if direction == -1:
                if target_vehicle.row - 2 < 0:
                    return False
                next_tile = self.get_vehicle_from_location(target_vehicle.row - 1, target_vehicle.col)

            # move down v
            elif direction == 1:
                if target_vehicle.row + target_vehicle.size > self.width:
                    return False
                next_tile = self.get_vehicle_from_location(target_vehicle.row + target_vehicle.size, target_vehicle.col)
            
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
        - Pre: `self.board` has vehicles on it, including `vehicle_id` and the move
        has been checked via `self.is_move_valid`.
        - Post: `vehicle_id` row and col are changed and `self.board` is updated.

        WARNING: THIS METHOD IS NOT SAFE. `Board.move_vehicle` should not be used 
        without first check the validity of the move via `Board.is_move_valid`. This
        method could move vehicles off the board or overwrite other vehicles. Bad 
        stuff. 
        
        TO DO: isn't this redundant as we already have two very similar methods? 
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
        Pre: Vehicle with `vehicle.id == "X"` exists.
        Post: Returns True if Vehicle with id X is as far right as is can go.
        """
        red_car = self.vehicle_dict["X"]
        if red_car.col == self.width - 1:
            return True
        return False

    def pickle_hash(self) -> int:
        """
        Returns unique number representing the current board state. Boards with 
        identical `self.pickle_hash()` are in the same state.
        - Pre: Board exists.
        - Post: Returns hash of the board state.
        """
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