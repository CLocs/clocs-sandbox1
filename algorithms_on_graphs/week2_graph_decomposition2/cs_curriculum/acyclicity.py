#Uses python3

import sys


def run_dfs(adj):
    # https://stackoverflow.com/questions/21669584/pre-and-post-numbers
    all_vs = list(range(len(adj)))
    visited = [0] * len(adj)
    pre = [0] * len(adj)
    post = [0] * len(adj)
    i_post = 1

    def dfs(v_e, i_e):
        visited[v_e] = 1
        i_e += 1
        pre[v_e] = i_e
        for v_next_e in adj[v_e]:
            if not visited[v_next_e]:
                i_e = dfs(v_next_e, i_e)
        i_e += 1
        post[v_e] = i_e
        return i_e

    for v in all_vs:
        if not visited[v]:
            i_post = dfs(v, i_post)

    return post


def run_explore(v, adj):
    visited = []

    def _explore(v, adj):
        visited.append(v)
        for v_next in adj[v]:
            if not visited[v_next]:
                _explore(v_next, adj)
    return visited


def strongly_connected_components(adj):
    # reverse G --> G-R
    adjR = [[] for _ in range(len(adj))]
    for iv, vs in enumerate(adj):
        for v in vs:
            adjR[v].append(iv)

    # run DFS on G-R
    post = run_dfs(adjR)

    # for v in V (post-order descending)
    post_reverse_tup = sorted([(e, i) for i, e in enumerate(post)], reverse=True)
    post_reverse = [i for v, i in post_reverse_tup]

    visited = [0] * len(adj)
    for v in post_reverse:
        if not visited[v]:
            # explore v
            v_explored = run_explore(v, adj)
            # visited vertices are SCC

    return 0


def dfs(v_e, i_e, visited, pre, post):
    visited[v_e] = 1
    i_e += 1
    pre[v_e] = i_e
    for v_next_e in adj[v_e]:
        if not visited[v_next_e]:
            i_e = dfs(v_next_e, i_e)
    i_e += 1
    post[v_e] = i_e
    return i_e



def acyclic(adj):
    unvisited = [True]*len(adj)
    visited = [False]*len(adj)
    visiting = [False]*len(adj)


    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
