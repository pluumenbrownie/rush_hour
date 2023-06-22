import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst
from classes.vehicle import * 

class BeamSearch(BreadthFirst):
    """ 
    This class gives implements a beam search algorithm
    """

    def amount_of_boxes(self, game:RushHour) -> int: 
        width = self.game.game_board.width
        # print(width) 
    
        # get location of red car 
        red_car = self.game.game_board.vehicle_dict["X"]
        
        # only interested in the colummn 
        col_red_car: int = red_car.col 

        # print(location_red_car)
        boxes = width - col_red_car

        return boxes

    def sort(self): 
        """ 
        Sort the children states > self.stack 
        Heuristic: states with red car closest to the exit are the best states 
        Pre: a stack with children states
        Post: a sorted stack with children states 
        """

        # this list needs to be sorted
        self.stack.sort(key=self.amount_of_boxes)


    def build_children(self, beamsize: int = 50) -> None: 
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
        self.sort()

        # if len(self.stack) > beamsize:
        #     print(len(self.stack))

        # if n is bigger than beam size: take only those at front of the queue 
        if len(self.stack) > beamsize: 
            self.stack = self.stack[:beamsize]

            

    







        



