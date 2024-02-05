from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        """
        :param v: a vertice to start traveling
        :param visited:  keep track of vertices visited
        :return: None
        """
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    def BFS(self, v):
        visited = [False] * (max(self.graph) + 1)
        queue = [v]
        visited[v] = True
        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True



if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)

    print("\n\nFollowing is BFS from (starting from vertex 2)")
    g.BFS(2)
