from Vertice import Vertice

class Aresta:

# *******************************************************
    def __init__(self, verticeOrigem, verticeFinal):
        self._verticeOrigem = verticeOrigem
        self._verticeFinal = verticeFinal
        verticeOrigem.adicionarVerticeAdj(verticeFinal)

# *******************************************************
    def getverticeOrigem(self) -> Vertice:
        return self._verticeOrigem

# *******************************************************
    def getverticeFinal(self) -> Vertice:
        return self._verticeFinal

# *******************************************************
    def getVertices(self):
        return self._verticeOrigem, self._verticeFinal

# *******************************************************
    def __str__(self):
        return f"[{self._verticeOrigem.getValue()},{self._verticeFinal.getValue()}]"

# *******************************************************

if __name__ == '__main__':

    verticeOrigem = Vertice(10)
    verticeFinal = Vertice(20)
    aresta = Aresta(verticeOrigem, verticeFinal)

    print(aresta)