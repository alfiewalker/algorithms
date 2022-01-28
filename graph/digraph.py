
class DiGraph:
    def __init__(self, vertices: 'list[int]') -> None:
        self.vertices = [[] for _ in range(vertices)]
        self.edges = 0

    def get_edges(self, v:int): 
        if v < 0 or v > len(self.vertices):
            raise Exception(f'Vertex {v} does not exist yet')
        return self.vertices[v]

    def vertex_count(self):
        return len(self.vertices)

    def edge_count(self):
        return self.edges

    def add_edge(self, v:int, w:int):
        v_edges = self.get_edges(v)
        v_edges.append(w) 
        self.edges += 1

    def add_edges(self, v:int, W:'list[int]'):
       for w in W:
          self.add_edge(v, w) 

    def degree(self, v):
        edges = self.get_edges(v) 
        return len(edges)

    def max_degree(self):
        max_ = 0
        for v in range(self.vertex_count()):
            max_ = max(max_, self.degree(v))
        return max_

    def __iter__(self):
        return iter(self.vertices)

    def __str__(self) -> str:
        print(f'Number of edges: {self.vertex_count()}')
        print(f'Number of vertices: {self.edge_count()}')
        for vertex, edges in self.vertices:
            e_str = "->".join(edges)
            print(f'{vertex}: {e_str}')

    