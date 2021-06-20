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
def bfs(vertices,adjacency_list,start):
    visited={i:False for i in vertices}
    queue=deque()
    queue.appendleft(start)
    visited[start]=True
    while queue:
        v=queue.pop()
        print(v,end=" ")
        for i in adjacency_list[v]:
            if(not visited[i]):
                queue.appendleft(i)
                visited[i]=True
vertices="ABCDEFG"
edges=[('A','B'),('B','A'),('A','E'),('E','A'),('A','D'),('D','A'),('D','E'),('E','D'),
       ('B','C'),('C','B'),('B','E'),('E','B'),('C','B'),('E','F'),('F','E'),('E','C'),('C','E'),
       ('C','G'),('G','C'),('F','G'),('G','F')]
k=get_list(vertices,edges)
print(k)
bfs(vertices,k,'A')
