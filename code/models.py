from typing import Any
import math as mt
import csv 


class Move():
    """ A move performed by a car """
    def __init__(self, target_id: str, direction: tuple[str, int]) -> None:
        self.target_id = target_id
        self.direction = direction


class Vehicle(): 
    """ Add a description """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        self.id = id
        self.orientation = orientation
        self.col = col
        self.row = row
        self.size = 0
    
    def get_tiles_occupied(self) -> list[tuple[int, int]]:
        coordinate_list = []
        for length in range(self.size):
            if self.orientation == "H":
                coordinate_list.append((self.col + length, self.row))
            else:
                coordinate_list.append((self.col, self.row + length))
        return coordinate_list

    def move(self, direction: int) -> None:
        assert direction == 1 or direction == -1
        if self.orientation == "H":
            self.col += direction
        else:
            self.row += direction
    
    def __repr__(self) -> str:
        if len(self.id) > 1:
            return f"{self.id * 2}"
        return f"{(self.id + ' ') * 2}"
        # return f"{self.col},{self.row}{self.orientation}"


class Car(Vehicle):
    """ A car with a direction """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        """ Creates a car object with a size, a direction and position on the board"""
        super().__init__(id, orientation, col, row)
        self.size = 2


class Truck(Vehicle):
    """ A truck with a direction"""

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        """ Creates a truck object with a size, a direction and position on the board"""
        super().__init__(id, orientation, col, row)
        self.size = 3

class RushHour():

    def __init__(self, width: int, board_file: str) -> None:
        self.game_board = Board(width)
        with open(board_file) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = True
            for line in csv_reader: 
                if header:
                    header = False
                    continue
                id = line[0].strip()
                orientation = line[1]
                col = int(line[2])
                row = int(line[3])
                length = int(line[4])
                print(id, orientation, col, row, length)
                if length == 2:
                    new_vehicle = Car(id, orientation, col, row)
                elif length == 3:
                    new_vehicle = Truck(id, orientation, col, row)
                else:
                    raise ValueError("Vehicle can only be length 2 or 3.")
                self.game_board.add_vehicle(new_vehicle)
        self.game_board.print_board()
    
    def show_board(self) -> None:
        self.game_board.print_board()
    
    def move_vehicle(self, vehicle_id: str, direction: int) -> None:
        move_viability = self.game_board.is_move_valid(vehicle_id, direction)
        print("Can move:", move_viability)
        if move_viability:
            self.game_board.move_vehicle(vehicle_id, direction)


class Board():
    """ Creates a board to which cars and trucks can be added """

    def __init__(self, width: int) -> None:
        """ Creates a empty board object with a width (6x6, 9x9, 12x12) and an exit. """
        self.width = width
        self.exit_height = mt.ceil(width / 2)
        self.exit_width = width - 1

        self.board = []
        for _ in range(width):
            empty_row = []
            for _ in range(width):
                empty_row.append(None)
            self.board.append(empty_row)
        self.print_board()

        self.vehicle_dict: dict[str, Car|Truck] = {}
        # self.load_gameboard("gameboards/Rushhour6x6_1.csv")
        
    
    def print_board(self) -> None:
        for row in self.board:
            print(row)
    
    def add_vehicle(self, vehicle: Car|Truck) -> None:
        coordinates_to_add = vehicle.get_tiles_occupied()
        for col, row in coordinates_to_add:
            self.board[row - 1][col - 1] = vehicle
        self.vehicle_dict[vehicle.id] = vehicle
    
    def is_move_valid(self, vehicle_id: str, direction: int) -> bool:
        target_vehicle = self.vehicle_dict[vehicle_id]
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
            else:
                raise ValueError("Invalid move direction.")
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
                raise ValueError("Invalid move direction.")
        else:
            raise ValueError("Invalid direction in vehicle.")
        print(next_tile)
        # return true if next_tile empty
        if next_tile:
            return False
        return True
    
    def move_vehicle(self, vehicle_id: str, direction: int) -> None:
        target_vehicle = self.vehicle_dict[vehicle_id]
        tiles_to_empty = target_vehicle.get_tiles_occupied()
        for col, row in tiles_to_empty:
            self.board[row - 1][col - 1] = None
        target_vehicle.move(direction)
        tiles_to_fill = target_vehicle.get_tiles_occupied()
        for col, row in tiles_to_fill:
            self.board[row - 1][col - 1] = target_vehicle
            


if __name__ == '__main__': 
    game = RushHour(12, "gameboards/Rushhour12x12_7.csv")
    game.move_vehicle('AB', -1)
    game.show_board()