<center><h1><strong>Graphs</strong><h1></center>
<h4>Definations<h4>
<ul>
<li>Graph is a non-linear data structure which consists of nodes/vertices/points and edges/lines/arcs(used to connect the pair of nodes).</li>
<li>Graph is a finite set of nodes and edges which is used to connect the pair of nodes.</li>
<li>Graph is pictorial representation of set of objects,where some pair of objects connected together by links.The interconnected objects are termed as nodes and links present between pair of objects termed as edges.</li>
<li>Graph is simply cyclic tree.</li>
</ul>

<h4>Example</h4>
Consider a graph pf vertices V(A,B,C,D,E) and edges E((A,B), (B,C), (C,E), (E,D), (D,B), (D,A)) is represented as follows
<img src="https://static.javatpoint.com/ds/images/graph-definition.png">

<h4>Applications</h4>
<ul>
<li>Graphs are used for developing recommandation system for social media applications and ecommerce applications</li>
<li>graphs are used to represent the flow of computation in computer science.</li>
<li>Google maps uses graphs for building transportation systems, where intersection of two(or more) roads are considered to be a vertex and the road connecting two vertices is considered to be an edge, thus their navigation system is based on the algorithm to calculate the shortest path between two vertices.</li>
<li>In world wide web,One page will connect to another through link. which is develeped based on graph data structure.</li>
</ul>

<h4>Types of Graphs</h4>
<ol>
	<li>Null</li>
	<li>Finite & Infinte</li>
	<li>Cyclic & Acyclic</li>
	<li>Simple & Multi</li>
	<li>Complete & Pseudo</li>
	<li>Connected & Disconnected</li>
	<li>Directed & Undirected</li>
	<li>Weighted & Unweighted</li>	
	<li>Dense & Sparse Graphs</li>
	<li>Bipartite Graph</li>
</ol>

<h4>1.Null Graph</h4>
A Graph which is defined as Null Graph if and only if it consists vertices/nodes and doesn't contains any edge between nodes/vertices.
<br>
A Graph consists of n nodes and zero vertices is called as Null Graph.
<br>
<h4>Example</h4>
<img src="https://static.javatpoint.com/tutorial/dms/images/types-of-graphs.jpg">
<h4>2.Finite Graph</h4>
A Graph which consists of finite number of vertices and edges is called as Finite Graph.
<br>
<h4>Example</h4>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simplegraph.png">
<br>
<h4>3.Infinte Graph</h4>
A Graph which Consists of infinite number of vertices and infinte number of edges called as Infinite Graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/graph2-4.png">
<h4>4.Cyclic Graph</h4>
A Graph Which consists of atleast one cycle is called as Cyclic Graph.
<img src="https://study.com/cimages/multimages/16/cyclic_graphs.png">
<h4>5.Acyclic Graph</h4>
A Graph which consists of No cycles is known as Acyclic Graph.
<img src="https://generalducky.github.io/images/Pic4.PNG">
<h4>6.Simple Graph</h4>
A Graph which consists of only one edge between any pair of vertices is known as simple graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simple1.png">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/simple2-1.png">
<h4>7.Multi Graph</h4>
A Graph which consits multiple edges between any pair of vertices and does not contain any self-loops is known as multi graph.
<img src="https://static.javatpoint.com/tutorial/dms/images/types-of-graphs2.jpg">
<h4>8.Complete Graph.</h4>
A graph which should consists of edge between every pair of vertices called Complete graph.Every complete graph is simple graph.
<br>
Degree of each node is number of vertices-1 
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types6.jpg.webp">
<h4>8.Pseudo Graph</h4>
A Graph which consists of atleast one self loop is known as Pseudo graph.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/pseudo-2.png">
<h4>9.Regular Graph</h4>
A graph which said to be regular if all vertices consists of equal degree.
<br>
A complete graph is regular but vice versa not possible.
<img src="https://media.geeksforgeeks.org/wp-content/uploads/regular-1.png">
<h4>9.Connected Graph</h4>
A Graph is said to be connected if there exists atleast one path between every pair of vertices.
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types12-1.jpg.webp">
<h4>10.DisConnected Graph</h4>
A Graph is said to be disconnected if it does not contain a path between atleast one pair of vertices.
<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/12/Graph-Types14.jpg.webp">
<h4>11.Directed Graph</h4>
A Graph is said to be Directed if and only if all edges contains direction and determines the traversal order.
<br>
A graph G = (V, E) with a mapping f such that every edge maps onto some ordered pair of vertices (Vi, Vj) is called Digraph. It is also called Directed Graph. Ordered pair (Vi, Vj) means an edge between Vi and Vj with an arrow directed from Vi to Vj
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/digraph.png">
<h4>12.Undirected Graph</h4>
A Graph is said to be undirected if and only if there is  no orientation/direction on the edges of graph.
Where a set of objects are connected, and all the edges are bidirectional. The below image showcases the undirected graph, 
It’s like the associativity of two Facebook users after connecting as a friend. Both users can refer and share photos, comment among each other
<img src="https://www.upgrad.com/blog/wp-content/uploads/2020/10/2.png">
<h4>13.Weighted Graph</h4>
Graphs whose edges or paths have values. All the values seen associated with the edges are called weights. Edges value can represent weight/cost/length.
<img src="https://miro.medium.com/max/469/1*tDJlwZ1x9TLibRvTlDQcEg.png">
<h4>14.Unweighted Graph</h4>
Where there is no value or weight associated with the edge. By default, all the graphs are unweighted unless there is a value associated.
<img src="https://miro.medium.com/max/471/1*EJLaKGGx2dd0NkwjHEPFEg.png">
<h4>15.Dense & Sparse Graphs</h4>
a dense graph is a graph in which the number of edges is close to the maximal number of edges. The opposite, a graph with only a few edges, is a sparse graph.
<img src="https://images.slideplayer.com/14/4318595/slides/slide_4.jpg">
<h4>16.Bipartite Graph</h4> 
If the vertex-set of a graph G can be split into two disjoint sets, V1 and V2 , in such a way that each edge in the graph joins a vertex in V1 to a vertex in V2 , and there are no edges in G that connect two vertices in V1 or two vertices in V2 , then the graph G is called a bipartite graph.
<img src="https://www.tutorialspoint.com/discrete_mathematics/images/complete_bipartite.jpg">
<h4>17.Complete Bipartite Graph</h4>
A complete bipartite graph is a bipartite graph in which each vertex in the first set is joined to every single vertex in the second set. The complete bipartite graph is denoted by Kx,y where the graph G contains x vertices in the first set and y vertices in the second set.
<img src="https://www.tutorialspoint.com/discrete_mathematics/images/complete_bipartite.jpg">

<h3>Graph Terminology</h3>
<h4>Vertex</h4>
Individual data element of a graph is known as Vertex.
<br>
Vertex is also known as node.
<h4>Edge</h4>
An Edge is path/line/connecting link betweet two vertices(Endpoints) in the graph.
<h4>Adjcent vertices</h4>
if two vertices are said to be adjacent if and only if they are endpoints of an edge.i.e those two vertices must and should form an edge.
<h4>Incident Edge</h4>
An Edge said to be an incident edge on a vertex,if the vertex is an endpoint of an edge.
<h4>Outgoing Edges</h4>
An Edge is said to be an outgoing edge of a vertx.If and only if edge is directed outwards from the vertex.
<h4>Incoming Edges</h4>
An Edge is said to be an Incoming edge of a vertx.if and only id edge is directd inwards to the vertex.
<h4>Degree</h4>
A degree of vertex is defined as number of edges which are incident/incoming on the vertex.
<h4>In-degree</h4>
Incoming degree of a vertex is defined as number of edges which are incoming to the vertex.
<h4>Out-degree</h4>
Outgoing degree of a vertex is defined as number of outgoing edges from thr vertex.
<h4>Parllel edges</h4>
if there are more than one edge between same pair of vertices.then they are called as parallel edges.
<h4>self-loop/cycle</h4>
self loop is an edge whose end vertices are equal.i.e if an edge exsited within same vertex.
<h4>Forest</h4>
A Graph with no cycles is known as Forest.
<h4>Simple Graph</h4>
a graph which does not contain any self loops and parellel edges.
<h4>Path</h4>
A Path is the sequence of successive edges between two nodes.
<h4>Length Of Path</h4>
Length Of Path id defined is number of successive edges between two nodes.
<h4>Simple Path</h4>
A Simple Path is the path which is formed by distinct vertices.
<h4>Source Vertex</h4>
A vertex whose in-degree is zero is called as source vertex.
<h4>Sink Vertex</h4>
A vertex whose out-degree is zero is called as sink vertex.
<h4>Strongly Connected Graph</h4>
A graph which contains a directed path from u to v and should contain a directed path from v to u for all pairs of vertices.
<h4>Weakly connected graph</h4>
A directed graph is said to be weakly connected if all directed edges are replaced by its undirected edges,it will form a connected graph.
<h4>Bridge</h4>
A bridge is an edge whose removal will result the disconnected graph.






