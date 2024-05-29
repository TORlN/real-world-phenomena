# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable

class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.nodes = set(range(num_nodes))
		self.edges = set(edges)
		self.neighbor_dict = {node: set() for node in self.nodes}
		for u, v in self.edges:
			self.neighbor_dict[u].add(v)
			self.neighbor_dict[v].add(u)
			

	def get_num_nodes(self) -> int:
		return len(self.nodes)
	def get_num_edges(self) -> int:
		return len(self.edges)

	def get_neighbors(self, node: int) -> Iterable[int]:
		return self.neighbor_dict[node]
	def get_degree(self, node: int) -> int:
		return len(self.neighbor_dict[node])

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
