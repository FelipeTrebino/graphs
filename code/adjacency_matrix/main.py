import networkx as nx
import matplotlib.pyplot as plt
from Grafo import Grafo

if __name__ == '__main__':

    grafo = Grafo(direcional=True, peso=True)
    
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')
    grafo.adicionarVertice('D')
    grafo.adicionarVertice('E')
    grafo.adicionarVertice('F')
    grafo.adicionarVertice('G')
    grafo.adicionarVertice('H')
    grafo.adicionarVertice('I')

    grafo.adicionarAresta('A','B', 100)
    grafo.adicionarAresta('B','A', 50)
    grafo.adicionarAresta('B','C', 24)
    grafo.adicionarAresta('D','A', 23)
    grafo.adicionarAresta('D','B', 34)
    grafo.adicionarAresta('D','C',1)
    grafo.adicionarAresta('D','E',0)
    grafo.adicionarAresta('D','F',40)
    grafo.adicionarAresta('D','G',45)
    grafo.adicionarAresta('D','H',20)
    grafo.adicionarAresta('D','C',47)
    grafo.adicionarAresta('C','I',25)
    grafo.adicionarAresta('I','F',15)
    grafo.adicionarAresta('H','G',33)
    grafo.adicionarAresta('G','E',22)
    grafo.adicionarAresta('E','A',90)
    grafo.adicionarAresta('F','H',102)

    edges = grafo.getArestas()
    nodes = grafo.getVertices()

    if grafo.isDirecional():
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    G.add_nodes_from(nodes)

    if grafo.isWeighted():
        for i in range(len(edges)):
            origem, destino, peso = edges[i]
            G.add_edge(origem, destino, weight=peso)
        pos = nx.spring_layout(G)  # Define a posição dos nós
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    else:
        G.add_edges_from(edges)
        pos = nx.spring_layout(G)  # Define a posição dos nós
    
    nx.draw_networkx(G, pos)
    plt.axis('off')
    plt.show()
    
    