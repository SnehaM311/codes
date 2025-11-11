from collections import deque

nodes = ['A','B','C','D','E']
idx = {n:i for i,n in enumerate(nodes)}

matrix = [
  [0,1,1,0,0],  
  [1,0,0,1,0],  
  [1,0,0,1,1],  
  [0,1,1,0,1],  
  [0,0,1,1,0],  
]
adj = {'A':['B','C'],'B':['A','D'],'C':['A','D','E'],'D':['B','C','E'],'E':['C','D']}

def dfs(start):
    vis=[False]*len(nodes); order=[]
    def go(i):
        vis[i]=True; order.append(nodes[i])
        for j,val in enumerate(matrix[i]):
            if val and not vis[j]: go(j)
    go(idx[start]); return order

def bfs(start):
    q=deque([start]); vis={start}; order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in adj.get(u,[]):
            if v not in vis:
                vis.add(v); q.append(v)
    return order

print("DFS from A:", dfs('A'))
print("BFS from A:", bfs('A'))
