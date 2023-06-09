import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst
from classes.vehicle import * 

class BeamSearch(BreadthFirst):
    """ 
    This class implements a beam search algorithm
    It sorts the states based on three heuristics: 
    - Distance from red car to exit 
    - Number of vehicles that are blocking the red car 
    - A combination of these two
    """

    def col_red_car(self, game:RushHour) -> int:
        """ 
        Get the location of the red car from the vehicle dictionary and return the row of the red car 
        """
        red_car = game.game_board.vehicle_dict["X"]
        col_red_car: int = red_car.col 

        return col_red_car
    
    def row_red_car(self, game:RushHour) -> int:
        """ 
        Get the location of the red car from the vehicle dictionary and return the row of the red car 
        """
        red_car = game.game_board.vehicle_dict["X"]
        row_red_car: int = red_car.row

        return row_red_car

    def amount_of_boxes(self, game:RushHour) -> int:
        """ 
        Get the amount of boxes that are between the red car and the exit (heuristic 1)
        """
        width = game.game_board.width 
        boxes = width - self.col_red_car(game)

        return boxes

    def sort_by_distance(self) -> None: 
        """ 
        Heuristic (h1): boards with the red car closest to the exit are the best boards 
        Pre: a stack with children states
        Post: a sorted stack with children states 
        """
        self.stack.sort(key=self.amount_of_boxes)

    def count_blocking_vehicles(self, game:RushHour) -> int: 
        """ 
        Count the number of vehicles that are blocking the red car (heuristic 2)
        """
        row_red_car: int = self.row_red_car(game)
        col_red_car: int = self.col_red_car(game)
        width = game.game_board.width 
        
        # Set count to 0 
        count = 0 

        # Loop through the boxes in front of the red car 
        for i in range(col_red_car, width): 
            # Look for vehicle in this sport 
            vehicle = game.get_vehicle_from_location(row_red_car, i)
            if vehicle: 
                count += 1
    
        return count

    def sort_by_blocking_vehicles(self) -> None:
        """ 
        Heuristic (h2): looks at the amount car that are blocking the red car on the board
        The less blocking vehicles, the better the board 
        Pre: a stack with children states
        Post: a sorted stack based on h2
        """
        self.stack.sort(key=self.count_blocking_vehicles)
    
    def combination_heuristic(self, game:RushHour) -> int: 
        """ 
        This combines the distance from the target vehicle and the numnber of vehicles
        that block the way to the exit (h1 and h2)
        The lower the score the better, the better
        """
        count = self.count_blocking_vehicles(game)
        amount_of_boxes = self.amount_of_boxes(game)

        # My "formula" (see images/h3_combination_heuristic.png)
        score = count * amount_of_boxes

        return score 
    
    def sort_by_h3(self) -> None:
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
            vehicle_id, direction = move
            self.game.process_turn(vehicle_id, direction)
            
            # Check if state is already been visited
            visited = self.game.get_board_hash()
            if visited not in self.visited_states:
                self.visited_states.add(visited)                    
                self.stack.append(copy.deepcopy(self.game))
            self.game.process_undo()

        # Creating a priority queue using heuristics
        if heuristic == "h1": 
            # Sort the stack so that the most promising are at the front (from short to long distance)
            self.sort_by_distance()
        elif heuristic == "h2": 
            # Sort the stack so that the states with the least blocking cars in front of red car are at the front of the queue
            self.sort_by_blocking_vehicles()
        else: 
            # Sort the stack with a combination of the two heuristics (from low to high)
            self.sort_by_h3()

        # If n is bigger than beam size: take only those at front of the queue 
        if int(len(self.stack)) > int(beam_size): 
            self.stack = self.stack[:int(beam_size)]
        

    def run(self, heuristic, beam_size, first_only: bool = False) -> int:
        """
        This method runs the beam search algorithm.
        """
        while self.stack:
            # If game is won print output to csv
            if self.game.is_won():
                self.check_solution(self.game)

            # Get next state            
            new_state = self.get_next_state()
            if first_only and self.game.is_won():
                break

            # Check solution
            self.check_solution(new_state)
            self.game = new_state 

            # Beam search needs input: beam size (int) and sorting method (h1, h2, h3)                         
            self.build_children(heuristic, beam_size)

        print(f"New best move count: {self.best_move_count}")
    
        return self.best_move_count