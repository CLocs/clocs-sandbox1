import sys


def acyclic(graph_adj):
    all_vs = list(range(len(graph_adj)))
    visited = [0] * len(graph_adj)
    rec_stack = [0] * len(graph_adj)

    def cyclic_dfs_helper(v_i):
        # Mark visited; add to stack
        visited[v_i] = 1
        rec_stack[v_i] = 1
        # DFS on neighbors
        for v_neighbor in graph_adj[v_i]:
            if not visited[v_neighbor]:
                # dive in
                if cyclic_dfs_helper(v_neighbor):
                    return True
            # in current search stack
            elif rec_stack[v_neighbor]:
                return True
        # Done visiting; remove from stack
        rec_stack[v_i] = False
        return False

    # Run search on all nodes
    is_acyclic = False
    for v in all_vs:
        if not visited[v]:
            is_acyclic = cyclic_dfs_helper(v)
        if is_acyclic:
            break

    return is_acyclic


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
