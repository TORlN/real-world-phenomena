from graph_algorithms import get_clustering_coefficient, get_degree_distribution, get_diameter
from graph import Graph
import matplotlib.pyplot as plt
import math
import random
import numpy as np
from typing import Iterable
from scipy.stats import linregress

def test_graph_algorithms(graph):
    clustering_coefficient = get_clustering_coefficient(graph)
    degree_distribution = get_degree_distribution(graph)
    diameter = get_diameter(graph)
    
    return clustering_coefficient, degree_distribution, diameter

def experiment_and_collect_data():
    sizes = np.logspace(3, 5, num=10, dtype=int)
    specific_sizes = np.array([1000, 10000, 100000])
    sizes = list(np.unique(np.concatenate((sizes, specific_sizes))))
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
    # Plot diameter vs. size with best-fit line
    plt.figure()
    plt.plot(sizes, diameters, marker='o', label='Data')
    plt.xscale('log')
    plt.yscale('log')

    # Best-fit line for diameter vs. size
    log_sizes = np.log(sizes)
    log_diameters = np.log(diameters)
    slope, intercept, r_value, p_value, std_err = linregress(log_sizes, log_diameters)
    fit_fn = np.poly1d([slope, intercept])
    plt.plot(sizes, np.exp(fit_fn(log_sizes)), linestyle='dotted', label=f'Fit: y={np.exp(intercept):.2f}x^{slope:.2f}, $R^2$={r_value**2:.2f}')

    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Diameter')
    plt.title('Diameter vs. Number of vertices (log-log scale)')
    plt.legend()
    plt.savefig('diameter_vs_size_log_log.png')
    plt.close()

    # Plot clustering coefficient vs. size with best-fit line
    plt.figure()
    plt.plot(sizes, clustering_coefficients, marker='o', label='Data')
    plt.xscale('log')

    # Best-fit line for clustering coefficient vs. size
    log_clustering_coefficients = np.log(clustering_coefficients)
    slope, intercept, r_value, p_value, std_err = linregress(log_sizes, log_clustering_coefficients)
    fit_fn = np.poly1d([slope, intercept])
    plt.plot(sizes, np.exp(fit_fn(log_sizes)), linestyle='dotted', label=f'Fit: y={np.exp(intercept):.2f}x^{slope:.2f}, $R^2$={r_value**2:.2f}')

    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Clustering Coefficient')
    plt.title('Clustering Coefficient vs. Number of vertices (log scale)')
    plt.legend()
    plt.savefig('clustering_coefficient_vs_size_log.png')
    plt.close()

    # Plot degree distribution for each size
    for i, degree_distribution in enumerate(degree_distributions):
        degrees = np.array(list(degree_distribution.keys()))
        counts = np.array(list(degree_distribution.values()))

        # Linear scale degree distribution
        plt.figure()
        plt.scatter(degrees, counts, label='Data')
        plt.xlabel('Degree')
        plt.ylabel('Number of vertices')
        plt.title(f'Degree Distribution for n={sizes[i]} (lin-lin scale)')
        plt.legend()
        plt.savefig(f'degree_distribution_n_{sizes[i]}_lin_lin.png')
        plt.close()

        # Log-log scale degree distribution
        plt.figure()
        plt.scatter(degrees, counts, label='Data')
        plt.xscale('log')
        plt.yscale('log')
        
        plt.xlabel('Degree')
        plt.ylabel('Number of vertices')
        plt.title(f'Degree Distribution for n={sizes[i]} (log-log scale)')
        plt.legend()
        plt.savefig(f'degree_distribution_n_{sizes[i]}_log_log.png')
        plt.close()


def generate_erdos_renyi_graph(n):
    p = 2 * math.log(n) / n
    edges = set()
    v = 1
    w = -1
    while v < n:
        r = random.random()
        w += 1 + int(math.log(1 - r) / math.log(1 - p))
        while w >= v and v < n:
            w -= v
            v += 1
        if v < n:
            if v < w:
                edges.add((v, w))
            else:
                edges.add((w, v))
    
    print(f"Generated graph with {n} nodes and {len(edges)} edges.")
    return Graph(n, edges)

def main():
    sizes, diameters, clustering_coefficients, degree_distributions = experiment_and_collect_data()
    plot_results(sizes, diameters, clustering_coefficients, degree_distributions)
    

if __name__ == "__main__":
    main()