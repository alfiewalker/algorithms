from core.graph_algorithms import ConnectedComponents
from core.graph import Graph
import pytest

"""
To Run:
pytest -q test_graph.py
"""
class TestGraph:
    def setup_class(self):
        self.G = Graph(13)
        G = self.G
        G.add_edges(0, [6, 2, 1, 5])
        G.add_edges(1, [0])
        G.add_edges(2, [0])
        G.add_edges(3, [5,4])
        G.add_edges(4, [5,6,3])
        G.add_edges(5, [3,4,0])
        G.add_edges(6, [0,4])
        G.add_edges(7, [8])
        G.add_edges(8, [7])
        G.add_edges(9, [11,10,12])
        G.add_edges(10, [9])
        G.add_edges(11, [9,12])
        G.add_edges(12, [11,9])

    def test_should_count_vertices(self):
        """ Count the number of vertices """
        assert self.G.vertex_count() == 13

    def test_should_count_edges(self):
        """ Count the number of edges """
        assert self.G.edge_count() == 26

    def test_should_count_degrees(self):
        """ Count the degrees """
        assert self.G.degree(9) == 6

    def test_should_get_max_degrees(self):
        """ Get the max degree """
        assert self.G.max_degree() == 8

    def test_should_count_connected_components(self):
        """ Get the connected components """
        # assemble
        graph_algo = ConnectedComponents()
        # act
        component_count = graph_algo.run(self.G)
        # assert
        assert component_count == 4
