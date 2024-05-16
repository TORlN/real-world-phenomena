# explanations for these functions are provided in requirements.py

from graph import Graph
import random

def get_diameter(graph: Graph) -> int:
	r = random.randint(0, len(graph.nodes) - 1)
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
	raise NotImplementedError


def get_degree_distribution(graph: Graph) -> dict[int, int]:
	degree_dist = {}
	for node in graph.nodes:
		degree = len(graph.get_neighbors(node))
		if degree in degree_dist:
			degree_dist[degree] += 1
		else:
			degree_dist[degree] = 1
	return degree_dist

def bfs(graph, r):
	visited = set()
	queue = []
	queue.append(r)
	visited.add(r)
	dist = {}
	dist[r] = 0
	max_dist = 0
	while queue:
		s = queue.pop(0)
		for i in graph.get_neighbors(s):
			if i not in visited:
				queue.append(i)
				visited.add(i)
				dist[i] = dist[s] + 1
				if dist[i] > max_dist:
					max_dist = dist[i]

	return s, max_dist