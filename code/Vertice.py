

class Vertice:

    def __init__(self, value):
        self._adjacentes = []
        self._value = value

    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value

    def getAdjacentes(self) -> list:
        return self._adjacentes
    
    def adicionarVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            self._adjacentes.append(Vertice)
            return True
        return False
    
    def removeVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            try:
                self._adjacentes.pop(vertice)
            except:
                return False
            return True
        return False