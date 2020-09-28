#Uses python3

import sys


def reach(adj, x, y):
    visited = []
    queue = []

    queue += [x]
    while len(queue):
        curr = queue.pop(0)
        # Ignore if visited
        if curr in visited:
            continue
        else:
            # Mark visited and move to next and queue up
            visited += [curr]
            queue += adj[curr]
    # Output
    if y in visited:
        return 1
    else:
        return 0


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


def _get_adjacent_vertices(adj, v):

    pass

if __name__ == '__main__':
    # input = sys.stdin.read()

    # Hardcode inputs for ease

    # Path exists, output->1
    input = [
        4, 4,
        1, 2,
        3, 2,
        4, 3,
        1, 4,
        1, 4
    ]
    print('Reachability should be: 1')

    # # Path doesn't exist, output->0
    # input = [
    #     4, 2,
    #     1, 2,
    #     3, 2,
    #     1, 4
    # ]
    # print('Reachability should be: 0')

    # data = list(map(int, input))
    data = input

    n, m, adj, x, y = prep_inputs(data)
    reachability = reach(adj, x, y)
    print('Reachability = ', reachability)
