import copy

from classes.models import RushHour

class DepthFirst:
    """ 
    This class gives implements a depth first algorithm
    """
    
    def __init__(self, game:RushHour):
        """ 
        Initializes an algorithm with the rushhour game.
        """
        self.game = copy.deepcopy(game)
        
        # Make a stack with a begin state
        self.stack = [copy.deepcopy(self.game)]
        
        self.visited_states = set()
        
        self.best_solution = None
        self.best_move_count = float('inf')
        
    def get_next_state(self) -> RushHour:
        """
        Method that get the next state from the list of states.
        """
        return self.stack.pop()
    
    def build_children(self) -> None:
        """
        Creates all possible child-states and adds them to the list of states.
        """
        moves = []

        # Loop over all the different states the vehicles can be in
        for vehicle_id in self.game.get_vehicle_ids():
            for direction in [-1, 1]:
                if self.game.game_board.is_move_valid(vehicle_id, direction):
                    moves.append((vehicle_id, direction))

        # Loop over all the possible moves
        for move in moves:
            new_state = copy.deepcopy(self.game)
            vehicle_id, direction = move
            new_state.process_turn(vehicle_id, direction)
            
            #check if state is already been visited
            visited = new_state.get_board_hash()
            if visited not in self.visited_states:
                self.visited_states.add(visited)
                self.stack.append(new_state)
        
         
    def check_solution(self, new_state: RushHour) -> None:
        """
        Checks and accepts better solutions than the current solution.
        """
        if new_state.is_won():
            new_move_count = len(new_state.history)
            if new_move_count < self.best_move_count:
                self.best_solution = new_state
                self.best_move_count = new_move_count
                self.best_solution.show_board()
                self.best_solution.export_solution() 
    
    def run(self, first_only: bool = False) -> None:
        """
        This method runs the depth first algorithm.
        """
        
        while self.stack:
            # print("")
            # # self.game.show_board()
            # print(f"{self.game.is_won()=}")
            
            # If game is won print output to csv
            if self.game.is_won():
                self.check_solution(self.game)
            
            new_state = self.get_next_state()
            
            if first_only and self.game.is_won():
                break
            
            self.check_solution(new_state)
            self.game = new_state                            
            self.build_children()
        
        print(f"New best move count: {self.best_move_count}")   
        print("Done!")
        