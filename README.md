# Representações computacionais de grafos

Este repositório possui duas implementações diferentes de Grafos, cada uma com uma representação computacional diferente de grafos.

1. **Lista de adjacências:** Uma lista de adjacências é uma maneira simples de representar um grafo como uma lista de vértices. Consiste em um array de listas de tamanho |V| = n, em que cada lista do array representa um vértice e cada elemento da lista representa um vértice com o qual ele forma uma aresta. 
2. **Matriz de adjacências:** Uma matriz de adjacência é uma matriz bidimensional de dimensão |V| x |V| que representa o grafo mapeando o valor 1 na posição (i,j) se houver uma aresta do vértice i para o vértice j, e o valor 0,  caso esta aresta não exista. 

## Implementação:

A linguagem de programação escolhida para a implementação foi `Python`, pois é  amplamente utilizada e conhecida por sua simplicidade, legibilidade e extensa biblioteca de terceiros. Essas características tornam Python uma escolha interessante para implementar grafos. 

A implementação ocorreu utilizando programação orientada a objetos `(POO)`, pela modularidade e reutilização de código, encapsulamento, facilidade de manutenção e extensibilidade além da abstração envolvida.

Para cada implementação foi previsto uma série de operações básicas de grafos, estas são:

- Adicionar Vértice
- Remover Vértice
- Adicionar Aresta
- Remover Aresta
- Verificar se vértices são adjacentes
- Obter Grau de vértice
- Encontrar vértice no grafo
- Obter Grau médio do grafo
- Obter Grau mínimo do grafo
- Obter Grau máximo do grafo

Além disso, as duas implementações permitem o uso de grafo *direcional*, e a implementação via matriz de adjacências permite a implementação de *peso* em arestas.

## Lista de adjacências:
Para a implementação de lista de adjacências, foi implementado duas classes: *Vertice* e *Grafo*.

A classe Vertice possui uma lista de adjacências, que inclui todos vértices adjacentes, foi implementado um construtor que recebe o valor como parâmetro obrigatório, getters e métodos para remover e adicionar vértice adjacentes, verificar de vértice é adjacente e um método para verifiar o grau do vértice.

Apesar da bibliografia prever que complexidade para adicionar um vértice da lista de adjacências é `O(1)`, o sempre é verifica se o vértice já foi adicionado na lista, para evitar duplicidade, o que acarreta numa maior robustez da implementação, o que torna o a complexidade da operação `O(n)`, pois a lista passa a ser percorrida uma vez.

Já a classe Grafo possui apenas uma lista de vértices, e o parâmetro *direcional*, caso o objeto do tipo Grafo criado possua *arestas direcionadas*, passado no construtor, além dos métodos previstos no tópico de implementação.

Para instanciar um objeto do tipo Grafo basta efetuar a seguinte operação:

    grafo = Grafo()

Como padrão, o parâmetro *direcional* é *False*.

## Matriz de adjacências:
Como na implementação via lista de adjacências, foi implementado duas classes: *Vertice* e *Grafo*.

A classe Vertice, diferente de implementação anterior, não possui a informação de vértices adjacentes, servindo apenas para modularização e encapsulamento de atributos e métodos associados.

A classe Grafo nesta representação é responsável por armazenar a matriz que contém todas as informações de adjacências. E foi implementada através de 3 atributos principais:

- `arestas`: A matriz de adjacências dos vértices, é do tamanho N x N, tal que N é a quantidade de vértices.
- `arestas_indices`: Um dicionário que possui como índice o valor de cada vértice, e armazena o índice equivalente ao vértice na matriz de adjacências.
- `vertices`: Um lista que de objetos Vértice, que possui o índices equivalentes ao das colunas e linhas da matriz, tornando fácil o acesso dos objetos.

Além disso, o classe grafo possui 2 atributos relacionados ao tipo de grado, *direcional*, como na implementação anterior, e *peso*, que diz respeito ao peso atribuito as arestas da matriz.

Esta implementação também possui todas as operações descritas no tópico de *implementação*.

Como descrito na bibliografia, na implementação comum (sem peso), os valores preenchidos na matriz equivalem a existência ou ausência de adjacências entre os vértices, sendo 1 e 0 respectivamente. Já na implementação com peso, os valores preenchidos na matriz são equivalente ao peso atribuido, sendo 0 como valor padrão e `None` como ausência de adjacência. 

Uma informação relevante desta implementação é que a exclusão de um vértice, não pode acarretar na exclussão de uma linha e coluna da matriz, desta forma, a alternativa encontrada foi: Apagar a referência do dicionário `arestas_indices`, mudar todos os valores adjacência do vértice na matriz `arestas` para None e apontar o indice associado ao objeto na lista `vertices` para None, desta forma, apesar da matriz não mudar de tamanho, não temos mais a refência do vértice objeto grafo.  

Da mesma forma que a implementação anterior, para instanciar um objeto do tipo Grafo basta efetuar a seguinte operação:

    grafo = Grafo()

Como padrão, o parâmetros *direcional* e *peso* possuem o valor *False*.

## Como utilizar

Foi optado, por maior conveniênica o uso apenas dos valores do vértices como referência, ou seja, podemos nos referir a um vértice apenas utilizando o valor associado a ele, como incado nas operações abaixo:

    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarAresta('A', 'B')
    grafo.removeAresta('A','B')

Também podemos realizar as seguintes operações utilizando o grafo:

    grafo.getGrauMedio()
    grafo.getGrauMinimo()
    grafo.getGrauMaximo()    
    grafo.isDirecional()

Além de obter uma lista com de fato dos vértices e adjacências através de:

    grafo.getVertices()
    grago.getArestas()

O objeto vértice pode ser acessado pela seguinte operação:

    verticeA = grafo.encontraVertice('A')

Podemos obter informações a partir deste vértice, como atributos. Na implementação via lista de adjacências, como a informação dos vértices adjacentes se encontra no objeto vértice, podemos encontrar seu grau a partir da seguinte operação:

    verticeA.getGrau()

Já na implementação via matriz de adjacências, esta informação pode ser extraida a partir da seguinte chamada de método:

    grafo.getGrauVertice('A')

O mesmo ocorre para obter a informação se um vértice é adjacente ao outro:

    VerticeA.isAdjacente(VerticeB) -> lista de adjacências
    grafo.isAdjacente('A','B') -> matriz de adjacências

Caso o grafo seja do tipo *não direcional*  a operação:

    grafo.adicionarAresta('A', 'B')

Promoverá a adição, não só de B na lista de vértices adjacentes de A, mas como A na lista de B. Da mesma forma, a operação:

    grafo.removeAresta('A','B')

Irá ocasionar na remoção do ambos os vértices da listas de adjacências.

Na implementação via matriz de adjacências, podemos criar um grafo com peso nas arestas a partir da operação:

    grafo = Grafo(peso=True)

Dessa forma, passamos a atribuir peso as arestas, através da seguinte modificação:

    grafo.adicionarAresta('A', 'B', 10)

Podemos visualizar o estado atual do grafo no console através do comando:

    print(grafo)

Os códigos pode ser acessado no caminho **/code/adjacency_list** e **/code/adjanceny_matrix**, os programas podem ser testados a partir da execução dos módulos. Todos os métodos possuem comentários da lógica de implementação e complexidade dos algoritmos envolvidos.

Através da biblioteca *matplotlib.pyplot* podemos instânciar um grafo e o visualizar gráficamente através da execução dos programas **main.py**

<img src="https://raw.githubusercontent.com/FelipeTrebino/graphs/main/Grafo.png" width="600" alt="exemplo grafo1">
<img src="https://raw.githubusercontent.com/FelipeTrebino/graphs/main/Grafo2.png" width="600" alt="exemplo grafo2">
## Referencias:

[1] Th. H. Cormen, Ch. E. Leiserson, R. L. Rivest, C. Stein: **Introduction to Algorithms**. 2009
