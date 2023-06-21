import copy

from classes.models import RushHour
from algorithms.breadth_first import BreadthFirst

class BeamSearch(BreadthFirst):
    """ 
    This class gives implements a beam search algorithm
    """

    def __init__(self, game:RushHour, beam_size: int):
        """ 
        Initializes an algorithm with the rushhour game.
        """
        self.game = copy.deepcopy(game)
        # Make a queue with a begin state
        self.queue = [copy.deepcopy(self.game)]
        self.visited_states = set()
        self.beam_size = beam_size
        self.best_beams = []

    def build_children(self) -> None: 
        """""
        TO DO: add description of beam search
        Creates all possible child-states and adds them to the list of states.
        lengte van stack moet altijd hoogstens zo groot zijn als beam size
        """""
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
                # TO DO: hier ga ik iets aanpassen 
                self.stack.append(new_state)

            

    







        



