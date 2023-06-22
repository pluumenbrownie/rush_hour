from classes.models import RushHour
import random as rd


class Node:
    def __init__(self, board_hash: int, is_won: bool) -> None:
        self.board_hash: int = board_hash
        self.connections: dict[Node, tuple[str, int]] = {}
        self.dijkstra_value: int = 0
        self.heuristic_value: int = 0
        self.is_won: bool = is_won
    
    def __repr__(self) -> str:
        return str(self.board_hash)
    
    def __str__(self) -> str:
        output = self.__repr__()
        for other_node in self.connections:
            output += f"\n|-{repr(other_node)}"
        return output


class Graph:
    def __init__(self, game: RushHour) -> None:
        self.game = game
        self.starting_node: int = self.game.get_board_hash()
        self.nodes: dict[int, Node] = {
            self.starting_node: Node(self.starting_node, self.game.is_won())
        }
        self.vehicle_ids = self.game.get_vehicle_ids()
        
    def build_graph(self, iterations: int = 10000000) -> None:
        current_node = self.nodes[self.starting_node]
        for _ in range(iterations):
            random_vehicle = rd.choice(self.vehicle_ids)
            random_direction = rd.choice([-1, 1])
            success = self.game.process_turn(random_vehicle, random_direction)
            if not success:
                continue

            state_hash = self.game.get_board_hash()
            next_node = self.nodes.setdefault(state_hash, Node(state_hash, self.game.is_won()))

            current_node.connections.setdefault(next_node, self.game.history[-1][:2])
            # print(current_node)
            current_node = next_node
    
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


def test(game: RushHour):
    graph = Graph(game)
    graph.build_graph(10000000)
    graph.stats()