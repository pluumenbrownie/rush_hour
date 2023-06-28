from typing import Self
from classes.models import RushHour

import random as rd
import tqdm
import tracemalloc

class Node:
    """
    Node class for use in the graph.
    """

    def __init__(self, board_hash: int, is_won: bool) -> None:
        self.board_hash: int = board_hash
        self.connections: dict[Node, tuple[str, int]] = {}
        self.dijkstra_value: int = 0
        self.is_won: bool = is_won
        self.node_back: Node | None = None

    def __repr__(self) -> str:
        return str(self.board_hash)

    def __str__(self) -> str:
        output = self.__repr__()
        output += " <= " + repr(self.node_back)
        for other_node in self.connections:
            output += f"\n|-{repr(other_node)}"
        return output

    def __ne__(self, other: Self) -> bool:
        return not self.dijkstra_value == other.dijkstra_value

    def __gt__(self, other: Self) -> bool:
        return self.dijkstra_value > other.dijkstra_value

    def __ge__(self, other: Self) -> bool:
        return self.dijkstra_value >= other.dijkstra_value

    def __lt__(self, other: Self) -> bool:
        return self.dijkstra_value < other.dijkstra_value

    def __le__(self, other: Self) -> bool:
        return self.dijkstra_value <= other.dijkstra_value


class Graph:
    def __init__(self, board_size: int, file_location: str) -> None:
        self.board_size = board_size
        self.file_location = file_location
        self.game = RushHour(board_size, file_location)
        self.starting_node: int = self.game.get_board_hash()
        self.nodes: dict[int, Node] = {
            self.starting_node: Node(self.starting_node, self.game.is_won())
        }
        self.vehicle_ids = self.game.get_vehicle_ids()
        self.game.show_board()

    def reset_game(self) -> None:
        """
        Replace the current self.game with a new `RushHour`.
        """
        del self.game
        self.game = RushHour(self.board_size, self.file_location)

    def build_graph(self, max_iterations: int = 100_000, random_cutoff: int = 200) -> None:
        """
        Start construction of the state space graph. Graph is constructed by
        playing games with random moves.
        - `max_iterations`: int = 1000 - Amount of random games to run.
        - `random_cutoff`: int = 1000 - Amount of random moves per game.

        Example: for the defaults, `build_graph` will run 1000 games, each with
        1000 moves.
        """
        current_node = self.nodes[self.starting_node]
        progress_bar = tqdm.tqdm(range(max_iterations), desc=self.file_location)
        success = False
        
        for _ in progress_bar:
            for _ in range(random_cutoff):
                while not success:
                    random_vehicle = rd.choice(self.vehicle_ids)
                    random_direction = rd.choice([-1, 1])
                    success = self.game.process_turn(random_vehicle, random_direction)
                success = False

                vehicle_moved, direction_moved, state_hash = self.game.history[-1]
                next_node = self.nodes.get(state_hash, None)
                if not next_node:
                    next_node = Node(state_hash, self.game.is_won())
                    self.nodes[state_hash] = next_node
                connection_exists = next_node in current_node.connections
                if not connection_exists:
                    connection_added = (vehicle_moved, direction_moved)
                    current_node.connections[next_node] = connection_added
                    next_node.connections[current_node] = (
                        vehicle_moved,
                        direction_moved * -1,
                    )
                current_node = next_node
            self.reset_game()
            current_node = self.nodes[self.starting_node]
            
        self.reset_game()

    def reset_dijkstra(self) -> None:
        """
        Empty the variables used for the dijkstra algorithm.
        """
        for node in self.nodes.values():
            node.dijkstra_value = 0
            node.node_back = None

    def stats(self) -> None:
        """
        Prints the amount of nodes, the amount of connections and the amount of winning nodes.
        """
        print(f"{len(self.nodes)} nodes.")
        connection_total = 0
        winning_states = 0
        for node in self.nodes.values():
            connection_total += len(node.connections)
            if node.is_won:
                winning_states += 1
        print(f"{winning_states} winning state.")
        print(
            f"{connection_total} connections; {connection_total/len(self.nodes):.2f} per node avg."
        )
