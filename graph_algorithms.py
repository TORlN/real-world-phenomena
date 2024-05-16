# explanations for these functions are provided in requirements.py

import random
from graph import Graph
from collections import deque
from itertools import combinations

def get_diameter(graph: Graph) -> int:
	r = random.randint(0, len(graph.nodes) - 1)
	d_max = 0
	cache = {}
	while True:
		w, dist = bfs(graph, r, cache)
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
	degree_dist = {}
	for node in graph.nodes:
		degree = graph.get_degree(node)
		if degree in degree_dist:
			degree_dist[degree] += 1
		else:
			degree_dist[degree] = 1
	return degree_dist

def bfs(graph, r, cache):
    if r in cache:
        return cache[r]
    
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
    
    cache[r] = farthest_node, max_dist
    return farthest_node, max_dist
def num_two_edge(graph):
	num_two_edge = 0
	for node in graph.nodes:
		degree = graph.get_degree(node)
		num_two_edge += degree * (degree - 1) // 2

	return num_two_edge

def num_triangles(graph):
    L, degeneracy, N = degree_degeneracy(graph)
    triangle_count = 0
    for v in L:
        neighbors_v = graph.get_neighbors(v)
        for u, w in combinations(neighbors_v, 2):
            if w in graph.get_neighbors(u):
                triangle_count += 1
    return triangle_count // 3

def compute_degrees(graph):
	degree_dict = {}
	for node in graph.nodes:
		degree_dict[node] = graph.get_degree(node)
	return degree_dict

def degree_degeneracy(graph):
    num_nodes = len(graph.nodes)
    L = deque()
    degree = compute_degrees(graph)
    D = [set() for _ in range(num_nodes + 1)]
    H = set()
    N = {v: [] for v in graph.nodes}
    for v, d in degree.items():
        D[d].add(v)
    k = 0
    for _ in range(num_nodes):
        i = 0
        while not D[i]:
            i += 1
        k = max(k, i)
        v = D[i].pop()
        L.appendleft(v)
        H.add(v)
        for w in graph.get_neighbors(v):
            if w not in H:
                old_degree = degree[w]
                new_degree = old_degree - 1
                degree[w] = new_degree
                D[old_degree].remove(w)
                D[new_degree].add(w)
                N[v].append(w)
    return list(L), k, N