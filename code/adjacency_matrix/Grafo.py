from Vertice import Vertice

class Grafo:
    
# *******************************************************
    # Construtor da classe grafo, tem como valor padrão para direcional e peso (False)
    # direcional indica se o grafo é direcional e peso se as arestas do grafo possuem peso
    def __init__(self, direcional = False, peso = False):
        self._vertices = [] # Lista de vértices do grafo
        self._arestas = [] # Matriz de arestas do grafo
        self._arestas_indices = {} # Dicionário com os valores associados dos vértices que 
                                   # apontam ao indice do vértice equivalente na matriz (coluna) e lista de vértices
        self._direcional = direcional # Indica se o grafo é direcional
        self._peso = peso # Indica se o grafo possue peso nas arestas

# *******************************************************
    # Adiciona um vértice à lista de vértices e uma nova coluna e linha à matriz de adjacências, complexidade O(n) 
    def adicionarVertice(self, value):
        if self.encontraVertice(value) is None:
            # Adiciona o vértice na lista de vértices
            self._vertices.append(Vertice(value))
            # Adiciona uma linha para para coluna da matriz
            for i in range(len(self._arestas)):
                row = self._arestas[i]
                # Caso o grafo possua peso nas arestas, None indicara a ausência de adjacência na matriz
                if self._vertices[i] is None or self._peso:
                    row.append(None)
                else:
                    # Caso o grafo nao seja direcional, o número 0 indica a ausência de adjacência na matriz
                    row.append(0)
            # Adiciona uma nova coluna na matriz de adjacências de acordo com o tipo de grafo
            if self._peso:
                self._arestas.append([None]*(len(self._arestas)+1))
            else:
                self._arestas.append([0]*(len(self._arestas)+1))
                for i in range(len(self._vertices)):
                    # Verifica se a linha específica existe, pelo fato de vértice poderem ser apagados
                    if self._vertices[i] is None:
                        self._arestas[len(self._vertices)-1][i] = None
            self._arestas_indices[value] = len(self._arestas) - 1

# *******************************************************
    # Remove um vértice da lista de vértices e da matriz, como não podemos retirar linhas e colunas,
    # apagamos a referência do dicionário, mudamos todos os valores de adjacência para None e apontamos
    #  o objeto associado na lista de vértices para None, complexidade O(n)  
    def removeVertice(self, value) -> bool:
        # Verifica se o vértice existe na matriz
        if value in self._arestas_indices:
            # Armazena a posição do vértice na matriz e lista de vértices
            vertice_indice = self.encontraVerticePos(value)
            # Muda a linha equivalente ao vértice na matriz para None
            for row in self._arestas:
                row[vertice_indice] = None
            # Muda sua própria coluna na matriz para Nona 
            for a in range(len(self._arestas[vertice_indice])):
                self._arestas[vertice_indice][a] = None
            # Retira o vértice do dicionário de indices
            self._arestas_indices.pop(value)
            # Aponta o índice equivalente ao vértice para None
            self._vertices[vertice_indice] = None
        return False

# *******************************************************
    # Encontra o vértice através de seu valor e retorna o objeto da lista de vértices, complexidade O(n)
    def encontraVertice(self, value) -> Vertice|None:
        if value in self._arestas_indices:
            return self._vertices[self._arestas_indices.get(value)]
        return None 

# *******************************************************
    # Adiciona uma aresta na matriz de adjacências e adiciona um novo vértice caso o valor associado não 
    # seja correspondente a nenhum vértice existente, adiciona peso as arestas, caso o atributo peso seja True
    # Se o grafo for não direcional, o valor da adjacência é adicionado em ambas colunas dos vértices
    # complexidade O(n)
    def adicionarAresta(self, value1, value2, peso = None):
        vertice1 = self.encontraVerticePos(value1)
        vertice2 = self.encontraVerticePos(value2)

        if vertice1 is None:
            self.adicionarVertice(value1)
            vertice1 = self.encontraVerticePos(value1)

        if vertice2 is None:
            self.adicionarVertice(value2)
            vertice2 = self.encontraVerticePos(value2)

        if not self._peso:
            peso = 1
        else:
            if peso is None:
                peso = 0

        self._arestas[vertice1][vertice2] = peso
        if not self._direcional:
            self._arestas[vertice2][vertice1] = peso

# ******************************************************* 
    # Retorna o índice do vértice na matriz de adjacências e lista de vértices através do seu valor, complexidade O(n)
    def encontraVerticePos(self, value) -> int|None:
        if value in self._arestas_indices:
            return self._arestas_indices.get(value)
        return None

# *******************************************************
    #Remove uma aresta da matriz de adjacências, complexidade O(n)
    def removeAresta(self, value1, value2) -> bool:
        vertice1 = self.encontraVerticePos(value1)
        vertice2 = self.encontraVerticePos(value2)
        if vertice1 is not None and vertice2 is not None:
            if self.isWeighted():
                v = None
            else:
                v = 0
            if not self.isDirecional():
                self._arestas[vertice2][vertice1] = v
            self._arestas[vertice1][vertice2] = v
            return True
        return False

# *******************************************************
    # Retorna uma string para visualização do grafo, complexidade O(n^2)
    def __str__(self) -> str:
        outStr = "Vértices: ["
        for value, index in self._arestas_indices.items():
            outStr += f"({value} => {index}), "
        outStr = outStr[0:-2] + ']\n\nArestas:\n\n'
        outStr += '     |'
        for index in range(len(self._arestas)):
            outStr += f"  {index}   |"
        outStr = outStr[0:-2] + '\n'
        for index in range(len(self._arestas)):
            row = ''
            for i in range(len(self._arestas)):
                row += '  ' + f"{self._arestas[i][index]}" + max((4-len(str(self._arestas[i][index]))),0)*' ' + '|'
            
            outStr += f"   {index} |{str(row[0:-1])}\n"
        
        return outStr

# *******************************************************
    # Retorna uma lista com os valores dos vértices do grafo, complexidade O(n)  
    def getVertices(self) -> list:
        vertices = []
        for v in self._arestas_indices:
            vertices.append(v)
        return vertices
     
# *******************************************************
    # Retorna uma lista com os pares de adjacência dos vértices (arestas), complexidade O(n^2)
    def getArestas(self) -> list:
        arestas = []
        for val,i in self._arestas_indices.items(): 
            v = self._vertices[i]
            for a in self.obterAdjacentes(val):
                if not self.isDirecional():
                    if (a.getValue(),v.getValue()) not in arestas: 
                        arestas.append((v.getValue(),a.getValue()))
                else:
                   arestas.append((v.getValue(),a.getValue())) 
        return arestas

# *******************************************************    
    # Retorna os vértices adjacentes de um determinado vértice, complexidade O(n)
    def obterAdjacentes(self, value) -> list:
        v_pos = self.encontraVerticePos(value)
        vertices = []
        if v_pos is not None:
            for index in range(len(self._arestas[v_pos])):
                peso = self._arestas[v_pos][index]
                if self._peso and peso is not None:
                    vertices.append(self._vertices[index])
                if not self._peso and peso == 1:
                    vertices.append(self._vertices[index])
        return vertices

# *******************************************************
    # Retorna se o grafo é direcional, complexidade O(1)
    def isDirecional(self) -> bool:
        return self._direcional

# *******************************************************
    # Retorna se o grafo possui peso na arestas, complexidade O(1)
    def isWeighted(self) -> bool:
        return self._peso

# *******************************************************
    # Retorna o grau de um determinado vértice, complexidade O(n)
    def getGrauVertice(self, value) -> int:
        v_pos = self.encontraVerticePos(value)
        vertices = 0
        if v_pos is not None:
            for index in range(len(self._arestas[v_pos])):
                peso = self._arestas[v_pos][index]
                if self._peso and peso is not None:
                    vertices+=1
                if not self._peso and peso == 1:
                    vertices+=1
        return vertices

# *******************************************************
    # Retorna se dois vértices são adjacentes, complexidade O(n)
    def isAdjacente(self, value1, value2) -> bool:
        vertice_pos1 = self.encontraVerticePos(value1)
        vertice_pos2 = self.encontraVerticePos(value2)

        if vertice_pos1 is not None and vertice_pos2 is not None:
            if self._peso and self._arestas[vertice_pos1][vertice_pos2] is not None:
                return True
            if not self._peso and self._arestas[vertice_pos1][vertice_pos2] == 1:
                return True
        return False

# *******************************************************
    # Retorna o grau médio dos vértices, complexidade O(n)
    def getGrauMedio(self):
        soma = 0
        for v in self._arestas_indices:
            soma += self.getGrauVertice(v)
        return soma/len(self._arestas_indices)
    
# *******************************************************    
    # Retorna o grau mínimo dos vértices, complexidade O(n)
    def getGrauMinimo(self):
        if len(self._arestas_indices) > 0:
            grau_minimo = None
            for v in self._arestas_indices:
                if grau_minimo == None:
                    grau_minimo = self.getGrauVertice(v)
                else:
                    if self.getGrauVertice(v) < grau_minimo:
                        grau_minimo = self.getGrauVertice(v) 
            return grau_minimo
        return 0

# *******************************************************    
    # Retorna o grau máximo dos vértices, complexidade O(n)
    def getGrauMaximo(self):
        if len(self._arestas_indices) > 0:
            grau_maximo = None
            for v in self._arestas_indices:
                if grau_maximo == None:
                    grau_maximo = self.getGrauVertice(v)
                else:
                    if self.getGrauVertice(v) > grau_maximo:
                        grau_maximo = self.getGrauVertice(v) 
            return grau_maximo
        return 0

# *******************************************************
    # Retorna o peso de uma determinada aresta, complexidade O(n)
    def getPesoAresta(self, value1, value2) -> None|int :
        vertice_pos1 = self.encontraVerticePos(value1)
        vertice_pos2 = self.encontraVerticePos(value2)

        if vertice_pos1 is not None and vertice_pos2 is not None:
            if self._peso and self._arestas[vertice_pos1][vertice_pos2] is not None:
                return self._arestas[vertice_pos1][vertice_pos2]
            if not self._peso and self._arestas[vertice_pos1][vertice_pos2] == 1:
                return 1
        None



# *******************************************************
# Programa de testes da classe grafo
if __name__ == '__main__':

    grafo = Grafo(peso=True)

    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')
    grafo.adicionarVertice('D')

    print(f"Grafo inicial:\n\n{grafo}")

    grafo.adicionarAresta('A', 'B',10)
    #grafo.adicionarAresta('B', 'A')
    grafo.adicionarAresta('B', 'C',32)
    grafo.adicionarAresta('D','A',4)
    grafo.adicionarAresta('D','B',104)
    grafo.adicionarAresta('D','C',65)

    print(f"Grafo inicial:\n\n{grafo}")

    print(f"Vértices adjacentes à A: {[v.getValue() for v in grafo.obterAdjacentes('A')]}")
    print(f"Vértices adjacentes à B: {[v.getValue() for v in grafo.obterAdjacentes('B')]}")
    print(f"Vértices adjacentes à C: {[v.getValue() for v in grafo.obterAdjacentes('C')]}")
    print(f"Vértices adjacentes à D: {[v.getValue() for v in grafo.obterAdjacentes('D')]}")

    grafo.removeAresta('A','B')
    print(f"\nGrafo removendo aresta ('A','B'):\n\n{grafo}")

    print(f"Vértices adjacentes à A: {[v.getValue() for v in grafo.obterAdjacentes('A')]}")
    print(f"Vértices adjacentes à B: {[v.getValue() for v in grafo.obterAdjacentes('B')]}")
    print(f"Vértices adjacentes à C: {[v.getValue() for v in grafo.obterAdjacentes('C')]}")
    print(f"Vértices adjacentes à D: {[v.getValue() for v in grafo.obterAdjacentes('D')]}")

    grafo.removeVertice('A')
    print(f"\nGrafo removendo vertice A:\n\n{grafo}") 

    print(f"Vértices adjacentes à A: {[v.getValue() for v in grafo.obterAdjacentes('A')]}")
    print(f"Vértices adjacentes à B: {[v.getValue() for v in grafo.obterAdjacentes('B')]}")
    print(f"Vértices adjacentes à C: {[v.getValue() for v in grafo.obterAdjacentes('C')]}")
    print(f"Vértices adjacentes à D: {[v.getValue() for v in grafo.obterAdjacentes('D')]}")

    grafo.adicionarVertice('E')
    grafo.adicionarAresta('D','E',1)
    print(f"\nGrafo adicionando vertice E:\n\n{grafo}") 

    print(f"Vértices adjacentes à A: {[v.getValue() for v in grafo.obterAdjacentes('A')]}")
    print(f"Vértices adjacentes à B: {[v.getValue() for v in grafo.obterAdjacentes('B')]}")
    print(f"Vértices adjacentes à C: {[v.getValue() for v in grafo.obterAdjacentes('C')]}")
    print(f"Vértices adjacentes à D: {[v.getValue() for v in grafo.obterAdjacentes('D')]}")
    print(f"Vértices adjacentes à E: {[v.getValue() for v in grafo.obterAdjacentes('E')]}")

    print(f"\nGrau vértice D: {grafo.getGrauVertice('D')}" )
    print(f"\nGrau Médio: {grafo.getGrauMedio()}" )
    print(f"\nGrau Máximo: {grafo.getGrauMaximo()}" )
    print(f"\nGrau Mínimo: {grafo.getGrauMinimo()}" )
    
    print(f"\nPeso Aresta ('B','C'): {grafo.getPesoAresta('B','C')}")
