#Uses python3

import sys


def number_of_components(adj):
    result = 0
    ccs = [-1] * len(adj)

    all_vs = list(range(len(adj)))

    # def _get_all_vertices(adj):
    #     flatten = [v for vs in adj for v in vs]
    #     all_vs = list(set(flatten))
    #     return all_vs
    # vs = _get_all_vertices(adj)

    # def _explore1(v, adj, cc):
    #     e_visited = []
    #     e_queue = []
    #     e_queue += [v]
    #     while len(e_queue):
    #         curr = e_queue.pop(0)
    #         ccs[curr] = cc
    #         if curr not in e_visited:
    #             e_visited += [curr]
    #             e_queue += adj[curr]

    # Explore a vertex and mark its CC number
    def _explore(v, adj, cc):
        visited[v] = 1
        ccs[v] = cc
        for v_next in adj[v]:
            if not visited[v_next]:
                _explore(v_next, adj, cc)

    # Number all CCs
    visited = [0] * len(adj)
    cc_num = 1
    for v in all_vs:
        if not visited[v]:
            _explore(v, adj, cc_num)
            cc_num += 1

    return max(ccs)

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
