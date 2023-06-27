from classes.models import RushHour
from algorithms.beam_search import BeamSearch
# import time
# import statistics as stat


def beamsearch_experiment(board_size: int, board: str, export: bool = False, repeat: int = 1):
    """
    Experiment of beam search 
    Because it is deterministic, we are only interested in one run of each board with each heuristic with a different statespace
    """

    # Make a csv file with the chosen board 
    with open(f"results/beam_search/beam_search_{board}.csv", 'w') as file:
        file.write(f"board, heuristic, beam size, states\n") 

        game = RushHour(board_size, f"gameboards/Rushhour{board}.csv")

        # for beam_size in (200, 500, 1000):  
        for beam_size in (10, 20, 50, 100, 150, 200, 250):  
            for heuristic in ('h1', 'h2', 'h3'):
                beamsearch_algorithm = BeamSearch(game)
                print(f"Before completing: {heuristic}, beam_size {beam_size}")
                n_states = beamsearch_algorithm.run(heuristic, beam_size)
                print(f"{heuristic}, beam_size {beam_size}, states: {n_states}")
                file.write(f"{board_size}, {heuristic}, {beam_size}, {n_states}\n")
    
    # # Make a csv with all of the boards 
    # board1 = "Rushhour6x6_1.csv"
    # board4 = "Rushhour9x9_4.csv"
    # board7 = "Rushhour12x12_7.csv"

    # # Make a csv file for board 1
    # with open(f"results/beam_search/beam_search_{board1}.csv", 'w') as file:
    #     file.write(f"board, heuristic, beam size, states\n") 

    #     game = RushHour(board_size, f"gameboards/Rushhour{board1}.csv")

    #     for beam_size in (10, 20, 50, 100, 150):  
    #         for heuristic in ('h1', 'h2', 'h3'):
    #             beamsearch_algorithm = BeamSearch(game)
    #             n_states = beamsearch_algorithm.run(heuristic, beam_size)
    #             print(f"{heuristic}, beam_size {beam_size}, states: {n_states}")
    #             file.write(f"{board_size}, {heuristic}, {beam_size}, {n_states}\n")
    
    # # Make a csv file with board 4
    # with open(f"results/beam_search/beam_search_{board4}.csv", 'w') as file:
    #     file.write(f"board, heuristic, beam size, states\n") 

    #     game = RushHour(board_size, f"gameboards/Rushhour{board4}.csv")

    #     for beam_size in (10, 20, 50, 100, 150):  
    #         for heuristic in ('h1', 'h2', 'h3'):
    #             beamsearch_algorithm = BeamSearch(game)
    #             n_states = beamsearch_algorithm.run(heuristic, beam_size)
    #             print(f"{heuristic}, beam_size {beam_size}, states: {n_states}")
    #             file.write(f"{board_size}, {heuristic}, {beam_size}, {n_states}\n")
    
    # # Make a csv file with board 7
    # with open(f"results/beam_search/beam_search_{board7}.csv", 'w') as file:
    #     file.write(f"board, heuristic, beam size, states\n") 

    #     game = RushHour(board_size, f"gameboards/Rushhour{board7}.csv")

    #     for beam_size in (10, 20, 50, 100, 150):  
    #         for heuristic in ('h1', 'h2', 'h3'):
    #             beamsearch_algorithm = BeamSearch(game)
    #             n_states = beamsearch_algorithm.run(heuristic, beam_size)
    #             print(f"{heuristic}, beam_size {beam_size}, states: {n_states}")
    #             file.write(f"{board_size}, {heuristic}, {beam_size}, {n_states}\n")
    


