from collections import defaultdict,deque
#edges = [['a','c'],['a','b'],['b','d'],['c','e'],['d','f'],['e',''],['f','']]
edges=[[0,1],[0,2],[1,3],[3,5],[5,4],[4,3]] #https://leetcode.com/problems/find-if-path-exists-in-graph/
source=0
pathlist = defaultdict(list)

#Creating Adjacency list using hashmap, here Leetcode style bidirectional graph, hence two appends
for u, v in edges:
    pathlist[u].append(v)
    pathlist[v].append(u)
visited=set()

stack=deque()
stack.append(source)
while stack:
    node = stack.popleft()    
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in pathlist[node]:
            if neighbour not in visited:
                stack.append(neighbour)
#expected op: 012354
