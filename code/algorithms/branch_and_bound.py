from classes.models import RushHour
from algorithms.depth_first import DepthFirst
from algorithms.random import Random
import copy

class BranchAndBound(DepthFirst):
    
    def __init__(self, game:RushHour, bound: int|float = float('inf')):
        """ 
        Initializes an algorithm with the rushhour game.
        """
        self.game = copy.deepcopy(game)
        
        # Make a stack with a begin state
        self.stack = [copy.deepcopy(self.game)]
        
        # self.visited_states = set()
        self.visited_states: dict[int, int] = {}
        
        self.best_solution = None
        self.best_move_count = bound

    def archive_check(self, visited: int, new_depth: int) -> bool:
        is_visited = visited not in self.visited_states or self.visited_states[visited] > new_depth
        return is_visited and new_depth < self.best_move_count 
    
    def build_children(self) -> None:
        """
        Creates all possible child-states and adds them to the list of states.
        """
        new_depth = len(self.game.history) + 1
        if new_depth > self.best_move_count:
            return
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
            if self.archive_check(visited, new_depth):
                self.visited_states[visited] = new_depth
                # Copying is delayed until we're sure it's necessary
                self.stack.append(copy.deepcopy(self.game))
            self.game.process_undo()
         
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
                print(f"New best solution: {self.best_move_count} moves.")
                self.best_solution.export_solution(output_name=self.output_file) 
    
    def run(self, first_only: bool = True, output_file: str = "results/output.csv") -> int|float:
        """
        This method runs the depth first algorithm.
        """
        self.output_file = output_file
        return super().run(first_only)
    
    def bound_guess(self, tries: int = 1000) -> None:
        """
        Run random solutions to find upper bound for best solution. Limits running time
        """
        print("Guessing bound.")
        moves: list[int] = []
        for _ in range(tries):
            game = copy.deepcopy(self.game)
            random_algorithm = Random(game)
                
            _, m = random_algorithm.run(export=False)
            m = random_algorithm.optimize_random()
            moves.append(m)
            
            if m == min(moves):
                self.best_move_count = m
                
        print(f"New bound: {self.best_move_count}")