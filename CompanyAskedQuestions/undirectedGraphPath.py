from collections import defaultdict

def undirectedPath(edges, src, dst):
    graph = buildGraph(edges)
    print(graph)
    visited = set()
    return hasPath(graph, src, dst, visited)

def buildGraph(edges):
    adjacency_list = defaultdict(list)
    for a, b in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    return adjacency_list

def hasPath(graph, src, dest, visited):
    if src == dest:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dest, visited):
            return True
    return False

# Example usage
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'l', 'm'))  # Output: True
