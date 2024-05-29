from graph_algorithms import get_clustering_coefficient, get_degree_distribution, get_diameter
from graph import Graph
import matplotlib.pyplot as plt
import math
import random
import numpy as np
from typing import Iterable

def test_graph_algorithms(graph):
    clustering_coefficient = get_clustering_coefficient(graph)
    degree_distribution = get_degree_distribution(graph)
    diameter = get_diameter(graph)
    
    return clustering_coefficient, degree_distribution, diameter

def experiment_and_collect_data():
    sizes = [1000, 10000, 100000]
    diameters = []
    clustering_coefficients = []
    degree_distributions = []
    
    for n in sizes:
        graph = generate_erdos_renyi_graph(n)
        clustering_coefficient, degree_distribution, diameter = test_graph_algorithms(graph)
        
        diameters.append(diameter)
        clustering_coefficients.append(clustering_coefficient)
        degree_distributions.append(degree_distribution)
        
        print(f"Size: {n}, Diameter: {diameter}, Clustering Coefficient: {clustering_coefficient}")
    
    return sizes, diameters, clustering_coefficients, degree_distributions

def plot_results(sizes, diameters, clustering_coefficients, degree_distributions):
    # Plot diameter vs. size
    plt.figure()
    plt.plot(sizes, diameters, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Diameter')
    plt.title('Diameter vs. Number of vertices (log-log scale)')
    plt.savefig('diameter_vs_size_log_log.png')
    plt.close()

    # Plot clustering coefficient vs. size
    plt.figure()
    plt.plot(sizes, clustering_coefficients, marker='o')
    plt.xscale('log')
    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Clustering Coefficient')
    plt.title('Clustering Coefficient vs. Number of vertices (log scale)')
    plt.savefig('clustering_coefficient_vs_size_log.png')
    plt.close()

    # Plot degree distribution for each size
    for i, degree_distribution in enumerate(degree_distributions):
        degrees = list(degree_distribution.keys())
        counts = list(degree_distribution.values())
        
        plt.figure()
        plt.scatter(degrees, counts)
        plt.xlabel('Degree')
        plt.ylabel('Number of vertices')
        plt.title(f'Degree Distribution for n={sizes[i]} (lin-lin scale)')
        plt.savefig(f'degree_distribution_n_{sizes[i]}_lin_lin.png')
        plt.close()

        plt.figure()
        plt.scatter(degrees, counts)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('Degree')
        plt.ylabel('Number of vertices')
        plt.title(f'Degree Distribution for n={sizes[i]} (log-log scale)')
        plt.savefig(f'degree_distribution_n_{sizes[i]}_log_log.png')
        plt.close()


def generate_erdos_renyi_graph(n):
    p = 2 * math.log(n) / n
    edges = set()
    v = 1
    w = -1
    while v < n:
        r = random.random()
        w = w + 1 + math.floor(math.log2(1-r) / math.log2(1-p))
        while w >= v and v < n:
            w -= v
            v += 1
        if v < n:
            edges.add((v, w))
    return Graph(n, edges)

def main():
    sizes, diameters, clustering_coefficients, degree_distributions = experiment_and_collect_data()
    plot_results(sizes, diameters, clustering_coefficients, degree_distributions)
    

if __name__ == "__main__":
    main()