from abc import ABC, abstractmethod
from core.digraph import DiGraph

class GraphAlgorithm(ABC):
    [abstractmethod]
    def run(self, graph:DiGraph):
        pass

class ConnectedComponents(GraphAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def run(self, graph: DiGraph):
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

class ShortestPathDFS(GraphAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    def _helper(self, graph, start, end, path, shortest):
        path = path + [start]
        if start == end:
            return path

        for edge in graph.get_edges(start):
            if edge not in path:
                new_edges = graph.get_edges(edge)
                if shortest == None or len(new_edges) < len(shortest):
                    new_path = self._helper(graph, edge, end, path, shortest)
                    if new_path != None:
                        shortest = new_path

        return shortest

    def run(self, graph: DiGraph, start, end):
        return self ._helper(graph, start, end, [], None)
