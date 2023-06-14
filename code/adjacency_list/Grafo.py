from Vertice import Vertice

class Grafo:
    
# *******************************************************
    # Construtor da classe Grafo, tem como valor padrão para direcional (False)
    #  que indica se o Grafo será direcional
    def __init__(self, direcional = False):
        self._vertices = {}
        self._direcional = direcional

# *******************************************************
    # Adiciona um vértice no dicionário de vértice utilizando seu valor associado como index, complexidade O(1)
    def adicionarVertice(self, value):
        if self.encontraVertice(value) is None:
            vertice = Vertice(value)
            self._vertices[value] = vertice

# *******************************************************
    # Remove um vértice do dicionário e o retira de todas as listas de vértices adjacentes, complexidade O(n)
    def removeVertice(self, value) -> bool:
        vertice = self.encontraVertice(value)
        if vertice is not None:
            for v in self._vertices:
                if v.isAdjacente(vertice):
                    v.removeVerticeAdj(vertice)
            self._vertices.pop(value)
            del(vertice)
            return True
        return False


# *******************************************************
    # Verifica se o vértice esta presente no dicionário de vértices e o retorna, complexidade O(n)
    def encontraVertice(self, value) -> Vertice|None:
        if value in self._vertices:
            return self._vertices.get(value)
        return None 

# *******************************************************
    # Adiciona uma aresta entre dois vértices, caso o valor indicado não seja correspondente a um vértice existente
    # um novo vértice é criado. Caso o grafo não seja direcional, os vértices são adicionados na lista de adjacências um do outro
    #, complexidade O(n)
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
    # Remove uma aresta entre dois vértices existentes do grafo, caso seja não direcional, os vértices são removidos de ambas listas 
    # de adjacências, complexidade O(n) 
    def removeAresta(self, value1, value2) -> bool:
        vertice1 = self.encontraVertice(value1)
        vertice2 = self.encontraVertice(value2)
        if vertice1 is not None and vertice2 is not None:
            if not self.isDirecional():
                vertice2.removeVerticeAdj(vertice1)
            return vertice1.removeVerticeAdj(vertice2)
        return False

# *******************************************************    
    # Retorna os vértices adjancentes de um determinado vértice, complexidade O(n)
    def obterAdjacentes(self, value) -> list:
        v = self.encontraVertice(value)
        if v is not None:
            return v.getAdjacentes()
        return []

# *******************************************************
    # Retorna uma lista com os valores dos vértices do grafo, complexidade O(n) 
    def getVertices(self) -> list:
        vertices = []
        for v in self._vertices:
            vertices.append(v)
        return vertices

# *******************************************************
    # Retorna uma lista com os pares de adjacência dos vértices (arestas), complexidade O(n^2)
    def getArestas(self) -> list:
        arestas = []
        for v in self._vertices.values():
            for a in v.getAdjacentes():
                if not self.isDirecional():
                    if (a.getValue(),v.getValue()) not in arestas: 
                        arestas.append((v.getValue(),a.getValue()))
                else:
                   arestas.append((v.getValue(),a.getValue())) 
        return arestas

# *******************************************************
    # Retorna se o grafo é direcional, complexidade O(1)
    def isDirecional(self) -> bool:
        return self._direcional

# *******************************************************
    # Retorna uma string para visualização do grafo, complexidade O(n)
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
    # Retorna o grau médio dos vértices, complexidade O(n)
    def getGrauMedio(self):
        soma = 0
        for v in self._vertices.values():
            soma += v.getGrau()
        return soma/len(self.getVertices())
    
# *******************************************************    
    # Retorna o grau mínimo dos vértices, complexidade O(n)
    def getGrauMinimo(self):
        if len(self._vertices) > 0:
            grau_minimo = None
            for v in self._vertices.values():
                if grau_minimo == None:
                    grau_minimo = v.getGrau()
                else:
                    if v.getGrau() < grau_minimo:
                        grau_minimo = v.getGrau() 
            return grau_minimo
        return 0

# *******************************************************    
    # Retorna o grau máximo dos vértices, complexidade O(n)
    def getGrauMaximo(self):
        if len(self._vertices) > 0:
            grau_maximo = None
            for v in self._vertices.values():
                if grau_maximo == None:
                    grau_maximo = v.getGrau()
                else:
                    if v.getGrau() > grau_maximo:
                        grau_maximo = v.getGrau() 
            return grau_maximo
        return 0

# *******************************************************
# Programa de testes da classe grafo
if __name__ == '__main__':

    # Cria um objeto grafo
    grafo = Grafo()
    # Adiciona os vértices do grafo
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')
    grafo.adicionarVertice('D')
    # Adiciona as arestas do grafo
    grafo.adicionarAresta('A', 'B')
    grafo.adicionarAresta('B', 'A')
    grafo.adicionarAresta('B', 'C')
    grafo.adicionarAresta('D','A')
    grafo.adicionarAresta('D','B')
    grafo.adicionarAresta('D','C')

    # Imprime uma visualização do grado no console
    print(f"Grafo inicial:\n\n{grafo}")

    # Remove uma aresta e imprime novamente uma visualização do grafo no console
    grafo.removeAresta('A','B')
    print(f"\nGrafo removendo aresta ('A','B'):\n\n{grafo}")

    # Remove uma vértice e imprime uma visualização do grafo no console
    grafo.removeVertice('A')
    print(f"\nGrafo removendo vertice A:\n\n{grafo}")
