import networkx as nx
import matplotlib.pyplot as plt
from Grafo import Grafo

if __name__ == '__main__':

    grafo = Grafo(direcional=True)
    
    """
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')
    grafo.adicionarVertice('D')

    grafo.adicionarAresta('A', 'B')
    grafo.adicionarAresta('B', 'A')
    grafo.adicionarAresta('B', 'C')
    grafo.adicionarAresta('D','A')
    grafo.adicionarAresta('D','B')
    grafo.adicionarAresta('D','C')

    edges = grafo.getArestas()
    nodes = grafo.getVertices()

    if grafo.isDirecional():
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)  # Define a posição dos nós
    nx.draw_networkx(G, pos)
    plt.axis('off')
    plt.show()
    """
    