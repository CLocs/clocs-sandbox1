import unittest
from algorithms_on_graphs.week1_graph_decomposition1.adding_exits_to_maze.connected_components import number_of_components

class TestCC(unittest.TestCase):

    def prep_inputs(self, input):
        data = list(map(int, input.split()))
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        return adj

    def test_cc2(self):
        input = '4 2 1 2 3 2'
        adj = self.prep_inputs(input)
        ccs = number_of_components(adj)
        self.assertTrue(ccs == 2)
