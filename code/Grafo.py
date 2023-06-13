from Aresta import Aresta
from Vertice import Vertice

class Grafo:
    
# *******************************************************
    def __init__(self, direcional = False):
        self._vertices = []
        self._direcional = direcional

# *******************************************************
    def adicionarVertice(self, value):
        if self.encontraVertice(value) is None:
            vertice = Vertice(value)
            self._vertices.append(vertice)

# *******************************************************
    def removeVertice(self, value) -> bool:
        vertice = self.encontraVertice(value)
        if vertice is not None:
            for v in vertice.getAdjacentes():
                v.removeVerticeAdj(vertice)
            self._vertices.remove(vertice)
            return True
        return False


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

    def removeAresta(self, value1, value2) -> bool:
        vertice1 = self.encontraVertice(value1)
        vertice2 = self.encontraVertice(value2)
        if vertice1 is not None and vertice2 is not None:
            if not self.isDirecional():
                vertice2.removeVerticeAdj(vertice1)
            return vertice1.removeVerticeAdj(vertice2)
        return False

# *******************************************************    
    def obterAdjacentes(self, value) -> list:
        v = self.encontraVertice(value)
        if v is not None:
            return v.getAdjacentes()
        return []

# *******************************************************
    def getVertices(self) -> list:
        vertices = []
        for v in self._vertices:
            vertices.append(v.getValue())
        return vertices

# *******************************************************
    def getArestas(self) -> list:
        arestas = []
        for v in self._vertices:
            for a in v.getAdjacentes():
                if not self.isDirecional():
                    if (a.getValue(),v.getValue()) not in arestas: 
                        arestas.append((v.getValue(),a.getValue()))
                else:
                   arestas.append((v.getValue(),a.getValue())) 
        return arestas

# *******************************************************
    def isDirecional(self) -> bool:
        return self._direcional

# *******************************************************
    def __str__(self) -> str:
        outStr = 'Vértices: ['
        for v in self.getVertices():
            outStr += f"{v}, "
        outStr = outStr[0:-2] + "]\nArestas: ["
        for a in self.getArestas():
            outStr += f"{a}, "
        outStr = outStr[0:-2] + "]"
        return outStr

# *******************************************************

if __name__ == '__main__':

    grafo = Grafo()
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')

    grafo.adicionarAresta('A', 'B')
    grafo.adicionarAresta('B', 'C')

    print(f"Grafo inicial:\n{grafo}")

    grafo.removeAresta('A','B')
    print(f"\nGrafo removendo aresta ('A','B'):\n{grafo}")

    grafo.adicionarAresta('A', 'B')
    grafo.removeVertice('A')
    print(f"\nGrafo removendo vertice A:\n{grafo}")
