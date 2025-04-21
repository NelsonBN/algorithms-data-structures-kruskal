class Disjoint:
    def __init__(self, n):
        # Create the forest with n vertices, each vertex is its own parent
        self.parents = [n] * n
        for i in range(n):
            self.parents[i] = i

        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            parent = self.parents[x]
            self.parents[x] = self.find(parent)

        parent = self.parents[x]
        return parent


    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # Already in the same set
            return

        # Union by rank: attach the smaller rank tree under the root of the higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        else:
            # Same rank, make one the parent and increment its rank
            self.parents[root_y] = root_x
            self.rank[root_x] += 1

        return

def kruskal(graph):
    # 1. Sort all edges in non-decreasing order of their weight
    graph.sort(key=lambda edge: edge[2])

    # Find the number of vertices
    n = 0
    for u, v, _ in graph:
        n = max(n, u, v)
    n += 1  # Assuming vertices are labeled from 0 to n-1

    # 2. Create an empty MST and a disjoint
    mst = []
    ds = Disjoint(n)

    # 3. Process edges in sorted order
    for u, v, weight in graph:
        # Check if including this edge creates a cycle
        root_u = ds.find(u)
        root_v = ds.find(v)
        if root_u != root_v:
            # Include the edge in MST
            mst.append((u, v, weight))
            # Merge the forests (sets)
            ds.union(u, v)

            # Stop when we have n-1 edges (complete MST)
            if len(mst) == n - 1:
                break

    return mst


# (u, v, weight)
example_graph = [
    (0, 1, 4),
    (0, 4, 4),
    (1, 2, 1),
    (1, 6, 6),
    (1, 3, 8),
    (2, 4, 5),
    (3, 5, 7),
    (3, 7, 3),
    (7, 6, 5)
]

mst = kruskal(example_graph)

print("Edges in the Minimum Spanning Tree:")
total_weight = 0
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with weight {weight}")
    total_weight += weight

print(f"Total weight of MST: {total_weight}")
