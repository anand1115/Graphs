<center><h1>Graph Represntation</h1></center>
<h4>Representation</h4>
We know graph is a finite set of vertices and edges.
<br>
Graph is the concept of how we are storing the graph in the computer memory.
<br>
A graph can be represented in three ways based on opertion that we are performing on the graph as follows.
<ul>
	<li>Adjacency Matrix</li>
	<li>Adjacency List</li>
	<li>Incidence Matrix</li>
	<li>Incidence  List</li>
</ul>
<h3>Adjacency Matrix</h3>
In this representation, the graph is represented using a matrix of size total number of vertices by a total number of vertices.
<br>
That means a graph with 4 vertices is represented using a matrix of size 4X4. In this matrix, both rows and columns represent vertices. This matrix is filled with either 1 or 0. 
<br>
Here, 1 represents that there is an edge from row vertex to column vertex and 0 represents that there is no edge from row vertex to column vertex.
<br>
<h4>Directed Graph</h4>
if A is adjacency matrix,aij=1 then there is a directed edge from vertex i to vertex j,
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Adjacency%20Matrix%202.jpg">
<h4>Undirected Graph</h4>
if A id adjacency matrix,aij=1 then there is a undiected edge from vertex i to vertex j and also there is another undirected edge from vertex i to vertex j
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Adjacency%20Matrix%201.jpg"> 
<h4>Weighted Graph</h4>
For weighted graph each cell is filled with that particular weight of edge instead of 1 as follows.
<br>
if any cell filled with 0,that means there is no edge between that vertices.
<br>
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations3.png">
<h4>Advantages</h4>
<ul>
	<li>Easy to understand and implements</li>
	<li>Checking whether an edge existed between two vertices/nodes takes O(1) time</li>
	<li>Removing an edge between two vertices/nodes takes O(1) time</li>
	<li>Adding an edge between two vertices/nodes takes O(1) time</li>
</ul>
<h4>Disadvantages</h4>
<ul>
	<li>Adding/removing a vertex to the existed graph will take more time O(v**2)(v=number of vertices)</li>
	<li>Consumes more space O(V**V) for even graph consists of less edges(sparse graph)</li>
</ul>
<h3>Adjacency List</h3>
Adjacency list is a linked representation.
<br>
In this representation, for each vertex in the graph, we maintain the list of its neighbors. It means, every vertex of the graph contains list of its adjacent vertices.
<br>
We have an array of vertices which is indexed by the vertex number and for each vertex v, the corresponding array element points to a singly linked list of neighbors of v.
<br>
Let's see the following directed graph representation implemented using linked list
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations5.png">
We can also implement this representation using array as follows:
<img src="https://static.javatpoint.com/tutorial/graph-theory/images/graph-representations6.png">
<h4>Advantages</h4>
<ul>
	<li>Adjacency list saves lot of space.</li>
	<li>Adding/deleting edge/vertex takes O(1) time</li>
	<li>Such kind of representation is easy to follow and clearly shows the adjacent nodes of node.</li>
</ul>
<h4>Disadavtages</h4>
<ul>
	<li>The adjacency list allows testing whether two vertices are adjacent to each other but it is slower to support this operation.</li>
</ul>
<h4>Incindence Matrix</h4>
In this representation, the graph is represented using a matrix of size total number of vertices by a total number of edges. That means graph with 4 vertices and 6 edges is represented using a matrix of size 4X6. In this matrix, rows represent vertices and columns represents edges. This matrix is filled with 0 or 1 or -1. Here, 0 represents that the row edge is not connected to column vertex, 1 represents that the row edge is connected as the outgoing edge to column vertex and -1 represents that the row edge is connected as the incoming edge to column vertex.
<br>
For example, consider the following directed graph representation...
<br>
<img src="http://www.btechsmartclass.com/data_structures/ds_images/Graph%20Incidence%20Matrix.jpg">
<br>


