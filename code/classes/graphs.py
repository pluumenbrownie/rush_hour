from code.classes.models import RushHour


class Node:
    def __init__(self, board_hash: int, winning: bool) -> None:
        self.board_hash: int = board_hash
        self.connections: dict[Node, tuple[str, int]]
        self.dijkstra_value: int = 0
        self.heuristic_value: int = 0
        self.winning: bool = winning
    
    def __repr__(self) -> str:
        return str(self.board_hash)
    
    def __str__(self) -> str:
        output = self.__repr__()
        for other_node in self.connections:
            output += f"\n|-{other_node}"
        return output


class Graph:
    def __init__(self, game: RushHour) -> None:
        self.starting_node: int = game.get_board_hash()
        self.nodes: dict[int, Node] = {
            self.starting_node: Node(self.starting_node, game.is_won())
        }
        
    


        
