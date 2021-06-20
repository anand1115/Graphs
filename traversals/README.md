<h1>Graph Traversals</h1>
<pre>
	Graph traversal is a technique used for a searching vertex in a graph. The graph traversal is also used to decide the order of vertices is visited in the search process. A graph traversal finds the edges to be used in the search process without creating loops. That means using graph traversal we visit all the vertices of the graph without getting into looping path.

	There are two graph traversal techniques and they are as follows...

	DFS (Depth First Search)
	BFS (Breadth First Search)
</pre>
<ul>
	<li>It is a technique visiting each vertex in the graph</li>
	<li>Finding all reachble nodes</li>
	<li>Finding the best reachble node and min max reachble node</li>
	<li>Finding the best path though nodes</li>
</ul>

<h1>Breadth First Search(level order traversal)</h1>
<p>Here we used to visit the all nodes of graph layer wise</p>
<p>Inorder to acheive the braedth first search here we are using the queue data structure.</p>
<p>Finnally the breadth first search will result the spanning tree as final result.</p>
<p>Spanning tree is a graph not having any loops</p>
<pre>
We use the following steps to implement BFS traversal...
Step 1 - Define a Queue of size total number of vertices in the graph.
Step 2 - Select any vertex as starting point for traversal. Visit that vertex and insert it into the Queue.
Step 3 - Visit all the non-visited adjacent vertices of the vertex which is at front of the Queue and insert them into the Queue.
Step 4 - When there is no new vertex to be visited from the vertex which is at front of the Queue then delete that vertex.
Step 5 - Repeat steps 3 and 4 until queue becomes empty.
Step 6 - When queue becomes empty, then produce final spanning tree by removing unused edges from the graph
</pre>

<pre>
	define queue q
	add any string vertex to queue
	mark start vertex as visited
	while q is not empty:
		pop the vertex from the queue which is at front end
		for i in each adjcent edge of popped vertx:
			add vertex i to queue
			mark vertex i as visited
</pre>