from classes.models import RushHour
from algorithms.beam_search import BeamSearch


def beamsearch_experiment(board_size: int, board: str, export: bool = False, repeat: int = 1):
    """
    Experiment of beam search. We want to know what beam sizes and what heuristics work the best
    Because it is deterministic, we are only interested in one run of each board with each heuristic with a different statespace

    Running this experiment on a 9x9 board took a very long time (it is possible it got stuck somewhere), therefore we only look at the results of the 6x6 boards. 
    We couldn't find a difference between the heuristics on the three different 6x6 boards. That could be due to the small size of the board. 
    """

    # make a csv file with the chosen board 
    with open(f"results/beam_search/beam_search_experiment_{board}.csv", 'w') as file:
        # write the first line 
        file.write(f"board, heuristic, beam size, states\n") 

        # create the board
        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")
 
        # if needed, you can adjust which beam size you want to try here 
        # for beam_size in (10, 20, 50, 100, 150, 200, 250, 300, 400):  
        for beam_size in (50, 100, 150):  
            for heuristic in ('h1', 'h2', 'h3'):
                beamsearch_algorithm = BeamSearch(game)
                # print(f"Before completing: {heuristic}, beam_size {beam_size}")
                n_states = beamsearch_algorithm.run(heuristic, beam_size)
                print(f"{heuristic}, beam_size {beam_size}, states: {n_states}")
                file.write(f"{board_size}, {heuristic}, {beam_size}, {n_states}\n")
