import unittest
from algorithms_on_graphs.week2_graph_decomposition2.cs_curriculum.acyclicity import acyclic

class TestAcyclicity(unittest.TestCase):
    def prep_inputs(self, input):
        data = list(map(int, input.split()))
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
        return adj

    def test_acyclic_1(self):
        input = '4 4 1 2 4 1 2 3 3 1'
        adj = self.prep_inputs(input)
        acyclic_result = acyclic(adj)
        self.assertTrue(acyclic_result == 1)

    def test_acyclic_2(self):
        input = '5 7 1 2 2 3 1 3 3 4 1 4 2 5 3 5'
        adj = self.prep_inputs(input)
        acyclic_result = acyclic(adj)
        self.assertTrue(acyclic_result == 0)
