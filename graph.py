# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.nodes = set(range(num_nodes))
		self.edges = set()
		for edge in edges:
			self.edges.add(edge)
		self.neighbor_dict = {}
		for node in self.nodes:
			self.neighbor_dict[node] = set()
			neighbors = set()
			for edge in self.edges:
				if edge[0] == node:
					neighbors.add(edge[1])
				if edge[1] == node:
					neighbors.add(edge[0])
			self.neighbor_dict[node] = neighbors
			

	def get_num_nodes(self) -> int:
		return len(self.nodes)
	def get_num_edges(self) -> int:
		return len(self.edges)

	def get_neighbors(self, node: int) -> Iterable[int]:
		return self.neighbor_dict[node]

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
