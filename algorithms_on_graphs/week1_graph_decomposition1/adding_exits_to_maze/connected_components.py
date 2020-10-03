#Uses python3

import sys


def number_of_components(adj):
    ccs = [-1] * len(adj)
    all_vs = list(range(len(adj)))
    visited = [0] * len(adj)

    # Explore a vertex and mark its CC number
    def _explore(v, adj, cc):
        visited[v] = 1
        ccs[v] = cc
        for v_next in adj[v]:
            if not visited[v_next]:
                _explore(v_next, adj, cc)

    # Number all CCs
    cc_num = 1
    for v in all_vs:
        if not visited[v]:
            _explore(v, adj, cc_num)
            cc_num += 1
    result = max(ccs)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
