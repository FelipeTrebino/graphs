
class Vertice:

# *******************************************************
    def __init__(self, value):
        self._adjacentes = []
        self._value = value

# *******************************************************
    def getValue(self):
        return self._value

# *******************************************************    
    def setValue(self, value):
        self._value = value

# *******************************************************
    def getAdjacentes(self) -> list:
        return self._adjacentes

# *******************************************************
    def adicionarVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            if not self.isAdjacente(vertice):
                self._adjacentes.append(vertice)
            return True
        return False

# *******************************************************
    def removeVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            if self.isAdjacente(vertice):
                self._adjacentes.remove(vertice)
            return True
        return False

# *******************************************************
    def isAdjacente(self, vertice) -> bool:
        if type(vertice) == Vertice:
            return vertice in self._adjacentes
        return False
    
# *******************************************************
        
    
if __name__ == '__main__':

    vertice1 = Vertice(10)
    vertice2 = Vertice(20)

    vertice1.adicionarVerticeAdj(vertice2)
    vertice2.adicionarVerticeAdj(vertice1)

    print(f"Vértice 1 ({vertice1.getValue()}): {[v.getValue() for v in vertice1.getAdjacentes()]}")
    print(f"Vértice 2 ({vertice2.getValue()}): {[v.getValue() for v in vertice2.getAdjacentes()]}")

    vertice1.removeVerticeAdj(vertice2)

    print(f"Vértice 1 ({vertice1.getValue()}): {[v.getValue() for v in vertice1.getAdjacentes()]}")
    print(f"Vértice 2 ({vertice2.getValue()}): {[v.getValue() for v in vertice2.getAdjacentes()]}")