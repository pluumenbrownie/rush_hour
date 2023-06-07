# Do we have to import anything? 
from typing import Any

class Board():
    """ Creates a board to which cars and trucks can be added """

    def __init__(self, width: int) -> None:
        """ Creates a empty board object with a width (6x6, 9x9, 12x12). """
        self.width = width

class Vehicle(): 
    """ Add a description """

    def __init__(self, id: str, direction: Any, column: int, row: int) -> None:
        self.id = id
        self.direction = direction
        self.column = column
        self.row = row


class Car(Vehicle):
    """ A car with a direction """

    def __init__(self, id: str, direction: Any, column: int, row: int) -> None:
        """ Creates a car object with a size, a direction and position on the board"""
        super().__init__(id, direction, column, row)
        self.size = 2


class Truck(Vehicle):
    """ A truck with a direction"""

    def __init__(self, id: str, direction: Any, column: int, row: int) -> None:
        """ Creates a truck object with a size, a direction and position on the board"""
        super().__init__(id, direction, column, row)
        self.size = 3

