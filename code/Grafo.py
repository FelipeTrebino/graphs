from Aresta import Aresta
from Vertice import Vertice

class Grafo:
    
# *******************************************************
    def __init__(self, direcional = False):
        self._vertices = []
        self._direcional = direcional

# *******************************************************
    def adicionarVertice(self, value):
        vertice = Vertice(value)
        self._vertices.append(vertice)

# *******************************************************
    def encontraVertice(self, value) -> Vertice|None:
        for v in self._vertices:
            if v.getValue() == value:
                return v
        return None

# *******************************************************
    def adicionarAresta(self, value1, value2):
        vertice1 = self.encontraVertice(value1)
        vertice2 = self.encontraVertice(value2)

        if vertice1 is None:
            self.adicionarVertice(value1)
        if vertice2 is None:
            self.adicionarVertice(value2)

        vertice1.adicionarVerticeAdj(vertice2)
        if not self._direcional:    
            vertice2.adicionarVerticeAdj(vertice1)

# *******************************************************
    
    def obterAdjacentes(self, value) -> list:
        v.encontraVertice(value)
        if v is not None:
            return v.getAdjacentes()
        return []

# *******************************************************

if __name__ == '__main__':

    grafo = Grafo()
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')

    grafo.adicionarAresta('A', 'B')
    grafo.adicionarAresta('B', 'C')

    v_adjacentesA = grafo.encontraVertice('A').getAdjacentes()
    v_adjacentesB = grafo.encontraVertice('B').getAdjacentes()
    v_adjacentesC = grafo.encontraVertice('C').getAdjacentes()

    print('Vértice A:')
    print([v.getValue() for v in v_adjacentesA])
    print('Vértice B:')
    print([v.getValue() for v in v_adjacentesB])
    print('Vértice C:')
    print([v.getValue() for v in v_adjacentesC])

