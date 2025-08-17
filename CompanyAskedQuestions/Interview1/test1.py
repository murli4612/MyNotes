# const graph ={
#     2: [3],
#     3: [1],
#     4: [0,1]
#     5: [0,2]
# };
from collections import defaultdict
def top_logical_sort(edges):
    adjacent = defaultdict(list)
    nodes = set()
    visited = set()
    stack =[]
    
    for point_x, point_y in edges:
        adjacent[point_x].append(point_y)
        nodes.add(point_x)
        nodes.add(point_y)
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neigh in adjacent[node]:
            dfs(neigh)
        stack.append(node)
            
    # for node in nodes:
    #     if node not in visited:
    #         dfs(node)
        
edges = { { 5, 0 }, { 5, 2 }, { 4, 0 }, { 4, 1 }, { 2, 3 }, { 3, 1 } }

sorted_value = top_logical_sort(edges)
print(sorted_value)