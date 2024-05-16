import random
from graph import Graph
import graph_algorithms as ga

def generate_random_graph(num_nodes, num_edges):
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            edges.add((u, v))
            edges.add((v, u))
    return Graph(num_nodes, list(edges))

def generate_complete_graph(num_nodes):
    edges = [(u, v) for u in range(num_nodes) for v in range(u + 1, num_nodes)]
    return Graph(num_nodes, edges)

def generate_sparse_graph(num_nodes, num_edges):
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            edges.add((u, v))
            edges.add((v, u))
    return Graph(num_nodes, list(edges))

# Test case generation
num_nodes = 1000 
num_edges = 5000  

random_graph = generate_random_graph(num_nodes, num_edges)
complete_graph = generate_complete_graph(num_nodes)
sparse_graph = generate_sparse_graph(num_nodes, num_edges // 10)

# Print the number of nodes and edges to verify
print("Random Graph:", random_graph.get_num_nodes(), "nodes,", random_graph.get_num_edges(), "edges")
print("Complete Graph:", complete_graph.get_num_nodes(), "nodes,", complete_graph.get_num_edges(), "edges")
print("Sparse Graph:", sparse_graph.get_num_nodes(), "nodes,", sparse_graph.get_num_edges(), "edges")

# Run functions on generated graphs
print("Diameter of Random Graph:", ga.get_diameter(random_graph))
print("Clustering Coefficient of Random Graph:", ga.get_clustering_coefficient(random_graph))
print("Degree Distribution of Random Graph:", ga.get_degree_distribution(random_graph))

print("Diameter of Complete Graph:", ga.get_diameter(complete_graph))
print("Clustering Coefficient of Complete Graph:", ga.get_clustering_coefficient(complete_graph))
print("Degree Distribution of Complete Graph:", ga.get_degree_distribution(complete_graph))

print("Diameter of Sparse Graph:", ga.get_diameter(sparse_graph))
print("Clustering Coefficient of Sparse Graph:", ga.get_clustering_coefficient(sparse_graph))
print("Degree Distribution of Sparse Graph:", ga.get_degree_distribution(sparse_graph))