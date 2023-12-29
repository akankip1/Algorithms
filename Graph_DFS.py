from collections import defaultdict
#edges = [['a','c'],['a','b'],['b','d'],['c','e'],['d','f'],['e',''],['f','']]
edges=[[0,1],[0,2],[1,3],[3,5],[5,4],[4,3]] #https://leetcode.com/problems/find-if-path-exists-in-graph/
source=0
pathlist = defaultdict(list)

#Creating Adjacency list using hashmap, here Leetcode style bidirectional graph, hence two appends
for u, v in edges:
    pathlist[u].append(v)
    pathlist[v].append(u)
visited=set()
    
def dfs(curr):
    print(curr) #output
    visited.add(curr)
    for node in pathlist[curr]:
        if node not in visited:
            dfs(node)
dfs(source)
#Iterative
# stack=deque()
# stack.append(source)
# while stack:
#     node = stack.pop()    
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in reversed(pathlist[node]):
#             if neighbour not in visited:
#                 stack.append(neighbour)

#expected output for given input: 013542
