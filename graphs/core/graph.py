
from core.digraph import DiGraph

class Graph(DiGraph):
    def __init__(self, vertices: 'list[int]') -> None:
        super().__init__(vertices)

    def add_edge(self, v:int, w:int):
        super().add_edge(v, w)
        w_edges = self.get_edges(w)
        w_edges.append(v)

    