import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst
from classes.vehicle import * 

class BeamSearch(BreadthFirst):
    """ 
    This class implements a beam search algorithm
    It sorts the states based on three sorting methodes: 
    - Distance from red car to exit 
    - Number of vehicles that are blocking the red car 
    - A combination of these two 
    """
    def col_red_car(self) -> int:
        """ 
        Get column of red car 
        """
 
        # get location of red car 
        red_car = self.game.game_board.vehicle_dict["X"]
        
        # only interested in the colummn 
        col_red_car: int = red_car.col 
        return col_red_car
    
    def row_red_car(self) -> int:
        """ 
        Get the row of the red car 
        """
        red_car = self.game.game_board.vehicle_dict["X"]
        row_red_car: int = red_car.row
        return row_red_car


    def amount_of_boxes(self, game:RushHour) -> int:
        """ 
        Get the amount of boxes that are between the red car and the exit 
        """
        # get width of board 
        width = self.game.game_board.width 
        # calculate boxes between red vehicle and exit 
        boxes = width - self.col_red_car()

        return boxes


    def sort_by_distance(self): 
        """ 
        Heuristic (h1): states with red car closest to the exit are the best states 
        Pre: a stack with children states
        Post: a sorted stack with children states 
        """
        self.stack.sort(key=self.amount_of_boxes)

    def count_blocking_vehicles(self, game:RushHour) -> int: 
        """ 
        Heuristic (h2): states with no or very little blocking vehicles are the best states
        """
        # get row and column of red car 
        row_red_car: int = self.row_red_car()
        col_red_car: int = self.col_red_car()
        width = self.game.game_board.width 
        
        # set count to 0 
        count = 0 

        # loop through the boxes in front of the red car 
        for i in range(col_red_car, width): 
            # print(i)
            # look for vehicle in this sport 
            vehicle = self.game.get_vehicle_from_location(row_red_car, i)
            if vehicle: 
                count += 1
    
        return count


    def sort_by_blocking_vehicles(self):
        """ 
        Using h2 to sort
        """
        self.stack.sort(key=self.count_blocking_vehicles)
    
    def combination_heuristic(self, game:RushHour) -> int: 
        """ 
        This combines the distance from the target vehicle and the numnber of vehicles
        that block the way to the exit
        
        The lower, the better
        """
        count = self.count_blocking_vehicles(game)
        amount_of_boxes = self.amount_of_boxes(game)

        # my "formula" 
        combination = count * amount_of_boxes

        return combination 
    
    def sort_by_h3(self):
        """ 
        Using combination heuristic to sort
        """
        self.stack.sort(key=self.combination_heuristic)
    
    def build_children(self, heuristic: str = 'h1', beam_size: int = 50) -> None: 
        """""
        Creates all possible child-states and adds them to the list of states.
        Length of stack needs to be at least as high as the beam size 
        """""
        moves = [] 
        
        # Loop over all the different states the vehicles can be in
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

        # creating a priority queue using heuristics

        if heuristic == "h1": 
            # sort the stack so that the most promising are at the front (from short to long distance)
            # print("beam search: sort by distance")
            self.sort_by_distance()

        elif heuristic == "h2": 
            # sort the stack so that the states with the least blocking cars in front of red car
            # print("beam search: sort by blocking vehicles")
            self.sort_by_blocking_vehicles()

        else: 
            # sort the stack with a combination of the two heuristics (from low to high)
            # print("beam search: combination of the two heuristics")
            self.sort_by_h3()

        # if n is bigger than beam size: take only those at front of the queue 
        if int(len(self.stack)) > int(beam_size): 
            self.stack = self.stack[:int(beam_size)]

    def run(self, heuristic, beam_size, first_only: bool = True) -> int:
        """
        This method runs the beam search algorithm.
        """
        # print(f"heuristic: {heuristic}")
        # print(f"beam size: {beam_size}")

        while self.stack:
            # If game is won print output to csv
            if self.game.is_won():
                self.check_solution(self.game)
            
            new_state = self.get_next_state()
            
            if first_only and self.game.is_won():
                break
            
            self.check_solution(new_state)
            self.game = new_state 
            # Beam search needs input: beam size (int) and sorting method (h1, h2, h3)                         
            self.build_children(heuristic, beam_size)
        
        print(f"New best move count: {self.best_move_count}")
    
        return self.best_move_count

            

    







        



