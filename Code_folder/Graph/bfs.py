# def iterative_bfs(graph,source):
#     queue = [source]
    
#     while queue:
#         current = queue.pop(0)
#         print(current)
#         for neighbour in graph[current]:
#             queue.append(neighbour)
    
    
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': ['F'],
#     'E': [],
#     'F': []
# }
# iterative_bfs(graph,"A")

def recursive_bfs(graph, queue):
    if not queue:
        return

    current = queue.pop(0)
    print(current)

    for neighbor in graph[current]:
        queue.append(neighbor)

    recursive_bfs(graph, queue)

# Sample graph (acyclic)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print("Recursive BFS (no visited):")
recursive_bfs(graph, ['A'])

        