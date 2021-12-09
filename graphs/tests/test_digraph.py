from core.algorithms import ConnectedComponents
from core.digraph import DiGraph
from core.algorithms import ShortestPathDFS
from test_data import TestData

# import pytest

"""
To Run:
pytest -q test_graph.py
"""
class TestDiGraph:
    def setup_class(self):
        self.G = TestData.create(DiGraph)

    def test_should_count_vertices(self):
        """ Count the number of vertices """
        assert self.G.vertex_count() == 13

    def test_should_count_edges(self):
        """ Count the number of edges """
        assert self.G.edge_count() == 26

    def test_should_count_degrees(self):
        """ Count the degrees """
        assert self.G.degree(9) == 3

    def test_should_get_max_degrees(self):
        """ Get the max degree """
        assert self.G.max_degree() == 4

    def test_should_count_connected_components(self):
        """ Get the connected components """
        # assemble
        graph_algo = ConnectedComponents()
        # act
        component_count = graph_algo.run(self.G)
        # assert
        assert component_count == 4

    def test_should_find_shortest_path_dfs(self):
        s_dfs = ShortestPathDFS()
        path = s_dfs.run(self.G, 0, 3)
        assert len(path)-1 == 2
