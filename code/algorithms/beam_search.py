import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst
from classes.vehicle import * 

class BeamSearch(BreadthFirst):
    """ 
    This class gives implements a beam search algorithm
    """

    def col_red_car(self) -> int: 
        # get location of red car 
        red_car = self.game.game_board.vehicle_dict["X"]
        
        # only interested in the colummn 
        col_red_car: int = red_car.col 

        return col_red_car
    
    def row_red_car(self) -> int: 
        # get location of red car 
        red_car = self.game.game_board.vehicle_dict["X"]
        
        # only interested in the colummn 
        row_red_car: int = red_car.row

        return row_red_car


    def amount_of_boxes(self, game:RushHour) -> int: 
        # get width of board 
        width = self.game.game_board.width 

        # calculate boxes between red vehicle and exit 
        boxes = width - self.col_red_car()

        return boxes

    def sort_by_distance(self): 
        """ 
        Sort the children states > self.stack 
        Heuristic: states with red car closest to the exit are the best states 
        Pre: a stack with children states
        Post: a sorted stack with children states 
        """

        # this list needs to be sorted
        self.stack.sort(key=self.amount_of_boxes)

    def count_blocking_vehicles(self, game:RushHour) -> int: 
        # get row and column of red car 
        row_red_car: int = self.row_red_car()
        col_red_car: int = self.col_red_car()
        width = self.game.game_board.width 

        # this is the amount of vehicles that are blocking the red car 
        count = 0 

        # loop through the boxes in front of the red car 
        for i in range(col_red_car, width): 
            print(i)
            # look for vehicle in this sport 
            vehicle = self.game.get_vehicle_from_location(row_red_car, i)
            if vehicle: 
                count += 1
    
        return count


    def sort_by_blocking_vehicles(self):
        self.stack.sort(key=self.count_blocking_vehicles)


    def build_children(self, beamsize: int = 10) -> None: 
        """""
        Creates all possible child-states and adds them to the list of states.
        lengte van stack moet altijd hoogstens zo groot zijn als beam size
        """""
        moves = [] 

        # Loop over all the different states the vehicles can be in
        # End: list of all states
        for vehicle_id in self.game.get_vehicle_ids():
            for direction in [-1, 1]:
                if self.game.game_board.is_move_valid(vehicle_id, direction):
                    moves.append((vehicle_id, direction))

        # Loop over all the possible moves
        for move in moves:
            # new_state = copy.deepcopy(self.game)
            vehicle_id, direction = move
            self.game.process_turn(vehicle_id, direction)
            
            # check if state is already been visited
            visited = self.game.get_board_hash()
            if visited not in self.visited_states:
                self.visited_states.add(visited)                    
                self.stack.append(copy.deepcopy(self.game))
            self.game.process_undo()

        # sort the stack so that the most promising are at the front 
        self.sort_by_distance()

        # sort the stack so that the states with the least blocking cars in front of red car 
        # self.sort_by_blocking_vehicles()

        # if len(self.stack) > beamsize:
        #     print(len(self.stack))

        # if n is bigger than beam size: take only those at front of the queue 
        if len(self.stack) > beamsize: 
            self.stack = self.stack[:beamsize]

            

    







        



