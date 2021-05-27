class Graph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges

    def get_adjacency_list_unordered(self):
        adj_list={}
        for i in self.edges:
            if i[0] in adj_list:
                adj_list[i[0]].add(i[1])
            else:
                adj_list[i[0]]=set(i[1])
            if i[1] in adj_list:
                adj_list[i[1]].add(i[0])
            else:
                adj_list[i[1]]=set(i[0])
        return adj_list
    
    def print_adjacency_list_unordered(self):
        for i in self.get_adjacency_list_unordered():
            print(i,"-->",*sorted(self.get_adjacency_list_unordered()[i]))
            
    def get_adjacency_list_ordered(self):
        adj_list={}
        for i in self.edges:
            if i[0] in adj_list:
                adj_list[i[0]].append(i[1])
            else:
                adj_list[i[0]]=[i[1]]
        return adj_list
    
    def print_adjacency_list_ordered(self):
        for i in self.get_adjacency_list_ordered():
            print(i,"-->",*self.get_adjacency_list_ordered()[i])

    def get_adjacency_list_ordered_weighted(self):
        adj_list={}
        for i in self.edges:
            if i[0] in adj_list:
                adj_list[i[0]].append((i[1],i[2]))
            else:
                adj_list[i[0]]=[(i[1],i[2])]
        return adj_list
    
    def print_adjacency_list_ordered_weighted(self):
        for i in self.get_adjacency_list_ordered_weighted():
            print(i,"-->",*self.get_adjacency_list_ordered_weighted()[i])

print("Unordered Graph")
vertices=['A','B','C','D','E']
edges=[('A','B'),('A','C'),('A','D'),('B','D'),('B','E'),('C','D'),('D','D'),('D','E')]
graph=Graph(vertices,edges)
graph.print_adjacency_list_unordered()
print("Ordered graph")
graph.print_adjacency_list_ordered()
print("Ordered graph with weight")
edges=[('A','B',3),('A','C',5),('A','D',6),('B','D',7),('B','E',8),('C','D',8),('D','D',9),('D','E',10)]
graph=Graph(vertices,edges)
graph.print_adjacency_list_ordered_weighted()

    
