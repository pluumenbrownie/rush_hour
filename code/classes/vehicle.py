from typing import Any

class Vehicle(): 
    """ 
    Add a description of a vehicle. 
    """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        """
        Initialize a vehicle with an ID, orientation, column, and row. 
        """
        self.id = id
        self.orientation = orientation
        self.col = col
        self.row = row
        self.size = 0
        self.color = "None"
    
    def get_tiles_occupied(self) -> list[tuple[int, int]]:
        """ 
        Return a list of coordinate tuples occupied by the vehicle. 
        """
        coordinate_list = []
        for length in range(self.size):
            if self.orientation == "H":
                coordinate_list.append((self.col + length, self.row))
            else:
                coordinate_list.append((self.col, self.row + length))
        return coordinate_list

    def move(self, direction: int) -> None:
        """ 
        Move the vehicle in the specified direction. 
        """
        assert direction == 1 or direction == -1
        if self.orientation == "H":
            self.col += direction
        else:
            self.row += direction
    
    def __repr__(self) -> str:
        """ 
        Return a string representation of the vehicle. 
        """
        if len(self.id) > 1:
            return f"{self.id * 2}"
        return f"{(self.id + ' ') * 2}"
    
    def __hash__(self) -> int:
        return hash((self.id, self.col, self.row))

class Car(Vehicle):
    """ 
    A car with a direction. 
    """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        """ 
        Initialize a car object with a size, a direction and position on the board. 
        """
        super().__init__(id, orientation, col, row)
        self.size = 2


class Truck(Vehicle):
    """ 
    A truck with a direction. 
    """

    def __init__(self, id: str, orientation: Any, col: int, row: int) -> None:
        """ 
        Initialize a truck object with a size, a direction and position on the board. 
        """
        super().__init__(id, orientation, col, row)
        self.size = 3