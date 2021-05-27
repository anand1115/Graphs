class Graph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges

    def get_adjacency_matrix_unordered(self):
        mat=[[0 for j in range(len(self.vertices))] for i in range(len(self.vertices))]
        for i in edges:
            start_point=ord(i[0])-ord('A')
            end_point=ord(i[1])-ord('A')
            mat[start_point][end_point]=1
            mat[end_point][start_point]=1
        return mat

    def get_adjacency_matrix_unordered_weighted(self):
        mat=[[0 for j in range(len(self.vertices))] for i in range(len(self.vertices))]
        for i in edges:
            start_point=ord(i[0])-ord('A')
            end_point=ord(i[1])-ord('A')
            mat[start_point][end_point]=i[2]
            mat[end_point][start_point]=i[2]
        return mat
    
    def get_adjacency_matrix_ordered(self):
        mat=[[0 for j in range(len(self.vertices))] for i in range(len(self.vertices))]
        for i in edges:
            start_point=ord(i[0])-ord('A')
            end_point=ord(i[1])-ord('A')
            mat[start_point][end_point]=1
        return mat
    
    def get_adjacency_matrix_ordered_weighted(self):
        mat=[[0 for j in range(len(self.vertices))] for i in range(len(self.vertices))]
        for i in edges:
            start_point=ord(i[0])-ord('A')
            end_point=ord(i[1])-ord('A')
            mat[start_point][end_point]=i[2]
        return mat
    
    def print_adjacency_matrix_unordered(self):
        for i in self.get_adjacency_matrix_unordered():
            print(*i,sep="  ")
            
    def print_adjacency_matrix_ordered(self):
        for i in self.get_adjacency_matrix_ordered():
            print(*i,sep="  ")
            
    def print_adjacency_matrix_ordered_weighted(self):
        for i in self.get_adjacency_matrix_ordered_weighted():
            print(*i,sep="  ")
    def print_adjacency_matrix_unordered_weighted(self):
        for i in self.get_adjacency_matrix_unordered_weighted():
            print(*i,sep="  ")
    
print("Unordered Graph")
vertices=['A','B','C','D','E']
edges=[('A','B'),('A','C'),('A','D'),('B','D'),('B','E'),('C','D'),('D','D'),('D','E')]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_unordered()
print("Unordered Graph with weights")
vertices=['A','B','C','D','E']
edges=[('A','B',2),('A','C',4),('A','D',5),('B','D',7),('B','E',9),('C','D',10),('D','D',4),('D','E',3)]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_unordered_weighted()
print("Ordered Graph")
vertices=['A','B','C','D','E']
edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','D'),('D','D'),('D','E')]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_ordered()
print("Ordered Graph with weights")
vertices=['A','B','C','D','E']
edges=[('A','B',2),('A','C',3),('B','D',4),('B','E',5),('C','D',6),('D','D',7),('D','E',8)]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_ordered_weighted()



