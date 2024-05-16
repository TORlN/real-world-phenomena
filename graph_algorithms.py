# explanations for these functions are provided in requirements.py

from graph import Graph
import random
from itertools import combinations
from collections import deque, defaultdict

def get_diameter(graph: Graph) -> int:
    if not graph.nodes:
        return 0

    r = random.choice(list(graph.nodes))
    d_max = 0
    while True:
        w, dist = bfs(graph, r)
        if dist > d_max:
            r = w
            d_max = dist
        else:
            break
    return d_max

def get_clustering_coefficient(graph: Graph) -> float:
    triangles = num_triangles(graph)
    two_edges = num_two_edge(graph)
    if two_edges == 0:
        return 0.0
    return 3 * triangles / two_edges

def get_degree_distribution(graph: Graph) -> dict[int, int]:
    degree_dist = defaultdict(int)
    for node in graph.nodes:
        degree = len(graph.get_neighbors(node))
        degree_dist[degree] += 1
    return dict(degree_dist)

def bfs(graph, r):
    visited = set()
    queue = deque([r])
    visited.add(r)
    dist = {r: 0}
    max_dist = 0
    farthest_node = r
    
    while queue:
        s = queue.popleft()
        current_dist = dist[s]
        for neighbor in graph.get_neighbors(s):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                dist[neighbor] = current_dist + 1
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, max_dist

def num_two_edge(graph):
    num_two_edge = 0
    for node in graph.nodes:
        degree = len(graph.get_neighbors(node))
        num_two_edge += degree * (degree - 1) // 2
    return num_two_edge

def num_triangles(graph):
    L, degeneracy, N = degree_degeneracy(graph)
    triangle_count = 0
    for v in L:
        for u, w in combinations(N[v], 2):
            if w in graph.get_neighbors(u):
                triangle_count += 1
    return triangle_count

def compute_degrees(graph):
    degree_dict = {}
    for node in graph.nodes:
        degree_dict[node] = len(graph.get_neighbors(node))
    return degree_dict

def degree_degeneracy(graph):
    L = []
    degree = compute_degrees(graph)
    max_degree = max(degree.values()) if degree else 0
    D = [[] for _ in range(max_degree + 1)]
    H = set()
    N = {v: [] for v in graph.nodes}

    for v, d in degree.items():
        D[d].append(v)

    k = 0
    for _ in range(len(graph.nodes)):
        i = 0
        while i < len(D) and not D[i]:
            i += 1
        k = max(k, i)
        v = D[i].pop()
        L.insert(0, v)
        H.add(v)

        for w in graph.get_neighbors(v):
            if w not in H:
                old_degree = degree[w]
                new_degree = old_degree - 1
                degree[w] = new_degree

                D[old_degree].remove(w)
                D[new_degree].append(w)

                N[w].append(v)

    return L, k, N





