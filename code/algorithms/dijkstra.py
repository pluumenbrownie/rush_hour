from classes.models import RushHour, count_statespace
from classes.graphs import Graph, Node
from sortedcontainers import SortedList


class Dijkstra:
    """
    Build a graph from a RushHour and run Dijkstras algorithm to find a solution.
    - `board_size`: int - size of the given board.
    - `board_file`: str - file location of given file.

    # To calculate solution:
    - Run `Dijkstra.buildgraph()`
    - Run `Dijkstra.run()`
    - Run `Dijkstra.export_solution()`
    """
    def __init__(self, board_size: int, board_file: str) -> None:
        self.board_size = board_size
        self.board_file = board_file
        self.graph = Graph(board_size, board_file)
    
    def build_graph(self, max_iterations: int = 1000, random_cutoff: int = 1000) -> None:
        """
        Start construction of the state space graph. Graph is constructed by 
        playing games with random moves.
        - `max_iterations`: int = 1000 - Amount of random games to run.
        - `random_cutoff`: int = 1000 - Amount of random moves per game.

        Example: for the defaults, `build_graph` will run 1000 games, each with
        1000 moves.
        """
        statespace = count_statespace(self.board_size, self.board_file)
        print(f"{statespace=}")
        print(f"Equals {statespace/(max_iterations*random_cutoff):.2f}x max_iterations*random_cutoff")
        self.graph.build_graph(max_iterations, random_cutoff=random_cutoff)
        # self.graph.build_graph_full_runs(max_iterations)
        self.graph.stats()
    
    def run(self) -> None:
        """
        Try to solve RushHour puzzle with the generated graph.
        Pre: `build_graph()` is run and contains winning state(s).
        """
        print("Started Dijkstra solver")
        nodes_considered = 0
        self.processing_queue = SortedList()
        starting_hash = self.graph.starting_node
        # visited_states: set[Node] = set()

        self.current_node = self.graph.nodes[starting_hash]
        while not self.current_node.is_won:
            self.extend_queue()
            self.current_node = self.processing_queue.pop(0)
            nodes_considered += 1
        
        print(f"Reached winning node. Concidered {nodes_considered} nodes.")
    
    def extend_queue(self) -> None:
        """
        Add connecting nodes of current node to `self.processing_queue`.
        Pre: `build_graph()` is run.
        """
        for connecting_node in self.current_node.connections:
            if connecting_node.node_back is None or connecting_node.dijkstra_value > self.current_node.dijkstra_value + 1:
                connecting_node.dijkstra_value = self.current_node.dijkstra_value + 1
                connecting_node.node_back = self.current_node
                self.processing_queue.add(connecting_node)
    
    def export_solution(self, export_file: str|None = "results/output.csv") -> int:
        """
        Write the found solution to a file and return the length of the solution.

        Pre: `run()` has been run and solution has been found.
        - export_file: str|None = "results/output.csv" - Path to output file. Pass
        `None` to prevent exporting.
        """
        moves: list[tuple[str, int]] = []
        while not self.current_node.board_hash == self.graph.starting_node:
            assert self.current_node.node_back
            previous_node = self.current_node.node_back
            step = previous_node.connections[self.current_node]
            moves = [step] + moves
            self.current_node = previous_node
        
        if export_file:
            with open(export_file, 'w') as file:
                file.write("car,move\n")
                for id, direction in moves:
                    file.write(f"{id},{direction}\n")
            print(f"Exported solution of {len(moves)} moves.")
        return len(moves)
