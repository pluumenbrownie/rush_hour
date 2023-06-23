from classes.models import RushHour, count_statespace
from classes.graphs import Graph, Node
from sortedcontainers import SortedList


class Dijkstra:
    """
    Builds a graph from a RushHour 
    """
    def __init__(self, board_size: int, board_file: str) -> None:
        self.board_size = board_size
        self.board_file = board_file
        self.graph = Graph(board_size, board_file)
    
    def build_graph(self) -> None:
        statespace = count_statespace(self.board_size, self.board_file)
        print(f"{statespace=}")
        print(f"Equals {statespace/10_000_000:.2f}x max_iterations")
        self.graph.build_graph(100_000_000)
        self.graph.stats()
    
    def run(self) -> None:
        self.processing_queue = SortedList()
        starting_hash = self.graph.starting_node
        # visited_states: set[Node] = set()

        self.current_node = self.graph.nodes[starting_hash]
        while not self.current_node.is_won:
            self.extend_queue()
            self.current_node = self.processing_queue.pop(0)
        
        print("Reached winning node.")
    
    def extend_queue(self) -> None:
        for connecting_node in self.current_node.connections:
            if connecting_node.node_back is None or connecting_node.dijkstra_value > self.current_node.dijkstra_value + 1:
                connecting_node.dijkstra_value = self.current_node.dijkstra_value + 1
                connecting_node.node_back = self.current_node
                self.processing_queue.add(connecting_node)
    
    def export_solution(self, export_file: str = "results/output.csv") -> None:
        moves: list[tuple[str, int]] = []
        while not self.current_node.board_hash == self.graph.starting_node:
            assert self.current_node.node_back
            previous_node = self.current_node.node_back
            step = previous_node.connections[self.current_node]
            moves = [step] + moves
            self.current_node = previous_node
        
        with open(export_file, 'w') as file:
            file.write("car,move\n")
            for id, direction in moves:
                file.write(f"{id},{direction}\n")
