from linkedlist import LinkedList

#A partir de la siguiente definición: Graph = Array(n,LinkedList())
#Diseñe una estrategia algorítmica para los siguientes problemas

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.weights = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.weights[u][v] = weight
        self.weights[v][u] = weight

#Ejercicio 23
def find_mandatory_edges(G: Graph):
    M = [[0 for _ in range(G.V)] for _ in range(G.V)]

    visited = [False] * G.V
    disc = [-1] * G.V
    low = [-1] * G.V
    parent = [-1] * G.V
    time = [0]

    def dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in range(G.V):
            if G.adj_matrix[u][v] == 1:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        M[u][v] = 1
                        M[v][u] = 1

                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

    dfs(0)
    return M

#Ejercicio 24
def shortest_path(G: Graph, s: int, v: int):
    dist = [float('inf')] * G.V
    dist[s] = 0
    prev = [None] * G.V
    visited = [False] * G.V

    for _ in range(G.V):
        u = min((dist[i], i) for i in range(G.V) if not visited[i])[1]
        visited[u] = True

        for neighbor in range(G.V):
            if G.adj_matrix[u][neighbor] == 1 and not visited[neighbor]:
                alt = dist[u] + G.weights[u][neighbor]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = u

    path = []
    current = v
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()

    return path if path[0] == s else None


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 4, 1)

    mandatory_edges = find_mandatory_edges(g)
    print("Matriz de aristas obligatorias:")
    for row in mandatory_edges:
        print(row)

    w = Graph(5)
    w.add_edge(0, 1, 8)
    w.add_edge(0, 2, 4)
    w.add_edge(1, 2, 1)
    w.add_edge(1, 3, 7)

    path = shortest_path(w, 0, 3)
    print("Camino más corto desde 0 hasta 3:", path)