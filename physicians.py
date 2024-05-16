import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.read_edgelist("data/moreno_innovation/out.moreno_innovation_innovation")

# Draw and customize G ('width' specifies edge width and 'alpha' specifies transparency of nodes)
nx.draw_networkx(G, node_size=150, font_size=6, width=0.4, alpha=0.75)

# Display G using matplotlib
# plt.show()

# Get the adjacency and laplacian matrices of G
adj = nx.adjacency_matrix(G)
lp = nx.laplacian_matrix(G)

# Spectrum
laplacian_spectrum = nx.laplacian_spectrum(G)
fiedler_value = nx.algebraic_connectivity(G)

print("The eigenvalues of L(G) are: " + np.array_str(laplacian_spectrum, suppress_small=True))
print(f'The fiedler value of G is: {fiedler_value}')