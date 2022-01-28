class TestData:
    [staticmethod]
    def create(graph_type):
        G = graph_type(13)
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
        return G