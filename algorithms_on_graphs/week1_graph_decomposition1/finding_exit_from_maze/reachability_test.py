#Uses python3

import sys
from algorithms_on_graphs.week1_graph_decomposition1.finding_exit_from_maze.reachability import reach


def prep_inputs(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return n, m, adj, x, y


def test_reachable1():
    # Path exists, output->1
    data = [
        4, 4,
        1, 2,
        3, 2,
        4, 3,
        1, 4,
        1, 4
    ]
    print('Reachability should be: 1')
    n, m, adj, x, y = prep_inputs(data)
    reachability = reach(adj, x, y)
    print('Reachability = ', reachability)


def test_unreachable1():
    # Path doesn't exist, output->0
    data = [
        4, 2,
        1, 2,
        3, 2,
        1, 4
    ]
    print('Reachability should be: 0')
    n, m, adj, x, y = prep_inputs(data)
    reachability = reach(adj, x, y)
    print('Reachability = ', reachability)


if __name__ == '__main__':
    test_reachable1()
    test_unreachable1()
