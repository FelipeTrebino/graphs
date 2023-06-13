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
        outStr += f"\nGrau médio: {self.getGrauMedio()}"
        outStr += f"\nGrau mínimo: {self.getGrauMinimo()}"
        outStr += f"\nGrau máximo: {self.getGrauMaximo()}"
        return outStr

# *******************************************************
    def getGrauMedio(self):
        soma = 0
        for v in self._vertices:
            soma += v.getGrau()
        return soma/len(self.getVertices())
    
# *******************************************************    
    def getGrauMinimo(self):
        if len(self._vertices) > 0:
            grau_minimo = self._vertices[0].getGrau()
            for i in range(1,len(self._vertices)):
                v = self._vertices[i]
                if v.getGrau() < grau_minimo:
                    grau_minimo = v.getGrau() 
            return grau_minimo
        return 0

# *******************************************************    
    def getGrauMaximo(self):
        if len(self._vertices) > 0:
            grau_maximo = self._vertices[0].getGrau()
            for i in range(1,len(self._vertices)):
                v = self._vertices[i]
                if v.getGrau() > grau_maximo:
                    grau_maximo = v.getGrau() 
            return grau_maximo
        return 0

# *******************************************************
if __name__ == '__main__':

    grafo = Grafo()
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


    print(f"Grafo inicial:\n\n{grafo}")

    grafo.removeAresta('A','B')
    print(f"\nGrafo removendo aresta ('A','B'):\n\n{grafo}")

    grafo.removeVertice('A')
    print(f"\nGrafo removendo vertice A:\n\n{grafo}")
