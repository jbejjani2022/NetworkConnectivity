import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a graph G using the list of edges in the jazz_musicians.txt file
G = nx.read_edgelist("data/arenas-jazz/jazz_musicians.txt")

# Draw and customize G ('width' specifies edge width and 'alpha' specifies transparency of nodes)
# nx.draw_networkx(G, node_size=150, font_size=6, width=0.4, alpha=0.75)
# print(G.number_of_edges())

# Display G
# plt.show()

# Construct the adjacency and Laplacian matrices of G
# adj = nx.adjacency_matrix(G)
# lp = nx.laplacian_matrix(G)

# Get and print the Laplacian spectrum
laplacian_spectrum = nx.laplacian_spectrum(G)
# print("The eigenvalues of L(G) are: " + np.array_str(laplacian_spectrum, suppress_small=True))

fiedler_value = nx.algebraic_connectivity(G)

# print("The eigenvalues of L(G) are: " + np.array_str(laplacian_spectrum, suppress_small=True))
# print(f'The fiedler value of G is: {fiedler_value}')
# print("The fiedler vector of G is: " + np.array_str(fiedler_vector, suppress_small=True))

# spectral_ordering = nx.spectral_ordering(G)
# print(len(spectral_ordering))
# print(spectral_ordering[:99])
# print(fiedler_vector[161])
# print([fiedler_vector[int(i)-1] for i in spectral_ordering[:99]])

fiedler_vector = nx.fiedler_vector(G)

positive_partition = []
negative_partition = []

# Sign Cut Approach
# for i in range(nx.number_of_nodes(G)):
#    if fiedler_vector[i] > 0:
#        positive_partition.append(str(i + 1))
#    else:
#        negative_partition.append(str(i + 1))

# print(positive_partition)
# print([fiedler_vector[i-1] for i in positive_partition])
# print(negative_partition)
# print([fiedler_vector[i-1] for i in negative_partition])

# Get the Fiedler Vector of G
fiedler_vector = nx.fiedler_vector(G)

# Declare lists to store the nodes in each partition
partition_one = []
partition_two = []

# Partition the graph using the Fiedler Vector according to our 'half and half' approach
for i in range(nx.number_of_nodes(G)):
    if fiedler_vector[i] < np.median(fiedler_vector):
        partition_one.append(str(i + 1))
    else:
        partition_two.append(str(i + 1))

# for i in ['198', '195', '77', '79']:
#    partition_one.remove(i)

# Construct and display the subgraph corresponding to our first partition of G
subgraph_one = nx.subgraph(G, partition_one)
# print(nx.algebraic_connectivity(subgraph_one))
# nx.draw_networkx(subgraph_one, node_size=150, font_size=6, width=0.4, alpha=0.75)
# plt.show()

subgraph_two = nx.induced_subgraph(G, partition_two)
print(nx.degree(subgraph_two, nbunch='67'))
print(nx.degree(G, nbunch='67'))
# print(nx.algebraic_connectivity(subgraph_two))
# print(nx.number_of_nodes(subgraph_two))

# nx.draw_networkx(subgraph_two, node_size=150, font_size=6, width=0.4, alpha=0.75)
# plt.show()

# Calculate Laplacian energy of graph G
E = nx.number_of_edges(G) * 2

# Initialize a list to store the Laplacian centrality of every node in G
laplacian_centralities = list(range(nx.number_of_nodes(G)))

# For every node in G
for node in nx.nodes(G):
    # Get a copy of G. This will be our subgraph.
    G_i = G.copy()
    # Remove current node from our subgraph
    G_i.remove_node(node)
    # Calculate the energy of the subgraph
    E_i = nx.number_of_edges(G_i) * 2
    # Calculate the centrality of the node
    C_i = (E - E_i) / E
    # Add the centrality to our list at index 'node - 1'
    laplacian_centralities[int(node)-1] = C_i


max_centrality = np.max(laplacian_centralities)
# print(max_centrality)
# for i in range(len(laplacian_centralities)):
#    if laplacian_centralities[i] == max_centrality:
#        print(i + 1)

# nodes with min centrality are 49, 162, 195, 197, 198

print(laplacian_centralities[4])
print(nx.degree(G, nbunch='5'))
# print(nx.degree(G, nbunch='195'))