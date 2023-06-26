from typing import Self
from classes.models import RushHour
import random as rd
import tqdm
import tracemalloc


class Node:
    def __init__(self, board_hash: int, is_won: bool) -> None:
        self.board_hash: int = board_hash
        self.connections: dict[Node, tuple[str, int]] = {}
        self.dijkstra_value: int = 0
        self.heuristic_value: int = 0
        self.is_won: bool = is_won
        self.node_back: Node|None = None
    
    def __repr__(self) -> str:
        return str(self.board_hash)
    
    def __str__(self) -> str:
        output = self.__repr__()
        output += " <= " + repr(self.node_back)
        for other_node in self.connections:
            output += f"\n|-{repr(other_node)}"
        return output
    
    # def __eq__(self, other: Self) -> bool:
    #     return self.dijkstra_value + self.heuristic_value == other.dijkstra_value + other.heuristic_value
    
    def __ne__(self, other: Self) -> bool:
        return not self.dijkstra_value + self.heuristic_value == other.dijkstra_value + other.heuristic_value
    
    def __gt__(self, other: Self) -> bool:
        return self.dijkstra_value + self.heuristic_value > other.dijkstra_value + other.heuristic_value
    
    def __ge__(self, other: Self) -> bool:
        return self.dijkstra_value + self.heuristic_value >= other.dijkstra_value + other.heuristic_value
    
    def __lt__(self, other: Self) -> bool:
        return self.dijkstra_value + self.heuristic_value < other.dijkstra_value + other.heuristic_value
    
    def __le__(self, other: Self) -> bool:
        return self.dijkstra_value + self.heuristic_value <= other.dijkstra_value + other.heuristic_value


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
        del self.game
        self.game = RushHour(self.board_size, self.file_location)
        
    def build_graph(self, max_iterations: int = 10_000_000, max_useless: int = 10_000) -> None:
        # tracemalloc.start()
        current_node = self.nodes[self.starting_node]
        useless = 0
        progress_bar = tqdm.tqdm(range(max_iterations), desc=self.file_location)
        for _ in progress_bar:
            random_vehicle = rd.choice(self.vehicle_ids)
            random_direction = rd.choice([-1, 1])
            success = self.game.process_turn(random_vehicle, random_direction)
            if not success:
                continue
            useless += 1

            vehicle_moved, direction_moved, state_hash = self.game.history[-1]
            next_node = self.nodes.get(state_hash, None)
            if not next_node:
                next_node = Node(state_hash, self.game.is_won())
                self.nodes[state_hash] = next_node
                useless = 0

            # connection_exists = current_node.connections.get(next_node, None)
            connection_exists = next_node in current_node.connections
            if not connection_exists:
                connection_added = (vehicle_moved, direction_moved)
                current_node.connections[next_node] = connection_added
                next_node.connections[current_node] = (vehicle_moved, direction_moved * -1)
                useless = 0
            # print(current_node)
            progress_bar.set_description(f"Useless moves: {useless}", refresh=False)
            if len(self.game.history) > 200:
                # print("Game history to large.")
                self.reset_game()
                current_node = self.nodes[self.starting_node]
                # useless = 0
                continue

            if useless > max_useless:
                print("Useless threshold reached. Stopping graph construction")
                break
            current_node = next_node
        # snapshot = tracemalloc.take_snapshot()
        # top_stats = snapshot.statistics('lineno')

        # print("[ Top 10 ]")
        # for stat in top_stats[:10]:
        #     print(stat)
        self.reset_game()
    
    def reset_dijkstra(self) -> None:
        """
        Empty the variables used for the dijkstra algorithm.
        """
        for node in self.nodes.values():
            node.dijkstra_value = 0
            node.node_back = None
    
    def stats(self) -> None:
        print(f"{len(self.nodes)} nodes.")
        connection_total = 0
        winning_states = 0
        for node in self.nodes.values():
            connection_total += len(node.connections)
            if node.is_won:
                winning_states += 1
        print(f"{winning_states} winning state.")
        print(f"{connection_total} connections; {connection_total/len(self.nodes):.2f} per node avg.")


def test(board_size: int, file_location: str):
    graph = Graph(board_size, file_location)
    graph.build_graph()
    graph.stats()
    graph.build_graph()
    graph.stats()