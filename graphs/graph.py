class Graph(dict):
    def __init__(self, vertex_list, edge_list):
        """
        Initializing graph data structure
        """
        for v in vertex_list:
            self[v] = set()
        for e in edge_list:
            self.add_edge(e)

    def add_edge(self, edge):
        """
        Add edge as a tuple of two vertices
        :type edge: tuple
        """
        self[edge[0]].add(edge[1])
        self[edge[1]].add(edge[0])

    def add_vertex(self, vertex):
        """
        Add vertex to graph
        :type vertex: set
        """
        self[vertex] = set()

    def delete_edge(self, edge):
        """
        Remove edge
        :param edge: tuple of two vertice
        """
        self[edge[0]].remove(edge[1])
        self[edge[1]].remove(edge[0])

    def delete_vertex(self, vertex):
        """
        Remove vertex
        :type vertex: set
        """
        temp_neighbour_set = self[vertex].copy()
        for neighbour_vertex in temp_neighbour_set:
            self.delete_edge((neighbour_vertex, vertex))
        del self[vertex]
