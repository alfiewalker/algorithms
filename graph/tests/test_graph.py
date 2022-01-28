from core.algorithms import ConnectedComponents
from core.graph import Graph
from test_data import TestData
# import pytest

"""
To Run:
pytest -q test_graph.py
"""
class TestGraph:
    def setup_class(self):
        self.G = TestData.create(Graph)

    def test_should_count_degrees(self):
        """ Count the degrees """
        assert self.G.degree(9) == 6

    def test_should_get_max_degrees(self):
        """ Get the max degree """
        assert self.G.max_degree() == 8
