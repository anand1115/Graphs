from collections import deque
def get_list(vertices,edges):
    final={}
    for i in vertices:
        for i,v in edges:
            if i in final:
                final[i].add(v)
            else:
                final[i]=set(v)
    return final
def dfs(vertices,list,start):
    visited={i:False for i in vertices}
    stack=[]
    stack.append(start)
    visited[start]=True
    while stack:
        v=stack.pop()
        print(v,end=" ")
        for i in list[v]:
            if not visited[i]:
                stack.append(i)
                visited[i]=True
vertices="ABCDEFG"
def dfs_recursive(list,vertex,visited):
    print(vertex,end=" ")
    visited[vertex]=True
    for i in list[vertex]:
        if not visited[i]:
            dfs_recursive(list,i,visited)
    

edges=[('A','B'),('B','A'),('A','E'),('E','A'),('A','D'),('D','A'),('D','E'),('E','D'),
       ('B','C'),('C','B'),('B','E'),('E','B'),('C','B'),('E','F'),('F','E'),('E','C'),('C','E'),
       ('C','G'),('G','C'),('F','G'),('G','F')]
k=get_list(vertices,edges)
print(k)
dfs(vertices,k,'A')
print()
dfs_recursive(k,'A',{i:False for i in vertices})
