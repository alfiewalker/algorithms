from abc import ABC, abstractmethod
from core.graph import Graph

class GraphAlgorithm(ABC):
    [abstractmethod]
    def run(self, graph:Graph):
        pass

class ConnectedComponents(GraphAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def run(self, graph: Graph):
        count = 0
        visited = [
            False for _ in range(graph.vertex_count())
        ]

        for v in range(graph.vertex_count()):
            if not visited[v]:
                edges = graph.get_edges(v)
                for edge in edges:
                    visited[edge] = True
                count += 1
            
        return count