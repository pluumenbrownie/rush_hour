# Do we have to import anything? 
from typing import Any

class Board():
    """ Creates a board to which cars and trucks can be added """

    def __init__(self, width: int) -> None:
        """ Creates a board object with a width. """
        self.width=width


class Car():
    """ A car with a direction """

    def __init__(self, direction: Any, column: int, row: int) -> None:
        """ Creates a car object with a size, a direction and position on the board"""
        self.size=2
        self.direction=direction
        self.column=column
        self.row=row


class Truck():
    """ A truck with a direction"""

    def __init__(self, direction: Any, column: int, row: int) -> None:
        """ Creates a truck object with a direction and position on the board"""
        self.size=3
        self.direction=direction
        self.column=column
        self.row=row

