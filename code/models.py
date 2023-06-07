from typing import Any
import math as mt
import csv 

class Board():
    """ Creates a board to which cars and trucks can be added """

    def __init__(self, width: int) -> None:
        """ Creates a empty board object with a width (6x6, 9x9, 12x12) and an exit. """
        self.width = width
        self.exit_height = mt.ceil(width / 2)
        self.exit_width = width - 1
        self.load_gameboard("npp")

    def load_gameboard(self, filename: str) -> Any: 
        with open("gameboards/Rushhour6x6_1.csv") as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader: 
                if line_count == 0:
                    print(f'Column names are {",".join(row)}')
                    line_count += 1
                else:
                    print(row)
            print(f'Processed {line_count} lines')


class Vehicle(): 
    """ Add a description """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        self.id = id
        self.orientation = orientation
        self.col = col
        self.row = row



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

if __name__ == '__main__': 
    bord = Board(6)