
class Vertice:

# *******************************************************
    # Construtor do vértice
    def __init__(self, value):
        self._adjacentes = []
        self._value = value

# *******************************************************
    # Retorna o valor associado ao vértice
    def getValue(self):
        return self._value

# *******************************************************
    # Retorna a lista de vértice adjacentes
    def getAdjacentes(self) -> list:
        return self._adjacentes

# *******************************************************
    # Adiciona um vértice a lista de vértices adjacentes, complexidade O(n)
    def adicionarVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            if not self.isAdjacente(vertice):
                self._adjacentes.append(vertice)
            return True
        return False

# *******************************************************
    # Remove um vértice da lista de vértices adjacentes, complexidade O(n)
    def removeVerticeAdj(self, vertice) -> bool:
        if type(vertice) == Vertice:
            if self.isAdjacente(vertice):
                self._adjacentes.remove(vertice)
            return True
        return False

# *******************************************************
    # Verifica se um determinado vértice é adjacente, complexidade O(n)
    def isAdjacente(self, vertice) -> bool:
        if type(vertice) == Vertice:
            return vertice in self._adjacentes
        return False
    
# *******************************************************
    # Determina o grau do vértice através da quantidade de vértices adjacentes, complexidade O(n)
    def getGrau(self) -> int:
        return len(self._adjacentes)
        
# Programa de testes da classe vértice    
if __name__ == '__main__':
    # Criação de dois vértices
    vertice1 = Vertice(10)
    vertice2 = Vertice(20)

    # Adicionando ambos na lista de vértices adjacentes
    vertice1.adicionarVerticeAdj(vertice2)
    vertice2.adicionarVerticeAdj(vertice1)

    # Verificando a lista de vértice adjanetes
    print(f"Vértice 1 ({vertice1.getValue()}): {[v.getValue() for v in vertice1.getAdjacentes()]}")
    print(f"Vértice 2 ({vertice2.getValue()}): {[v.getValue() for v in vertice2.getAdjacentes()]}")

    # Removendo um vértice da lista de vértice adjacentes
    vertice1.removeVerticeAdj(vertice2)

    # Verificando a lista de vértice adjanetes
    print(f"Vértice 1 ({vertice1.getValue()}): {[v.getValue() for v in vertice1.getAdjacentes()]}")
    print(f"Vértice 2 ({vertice2.getValue()}): {[v.getValue() for v in vertice2.getAdjacentes()]}")