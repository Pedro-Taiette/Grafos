class Grafo:
    def __init__(self):
        self.matriz_adjacencia = []
        self.num_vertices = 0

    def inserir_vertice(self):
        """Adiciona um novo vértice ao grafo"""
        self.num_vertices += 1

        for linha in self.matriz_adjacencia:
            linha.append(0)

        self.matriz_adjacencia.append([0] * self.num_vertices)

    def remover_vertice(self, vertice):
        """Remove um vértice do grafo"""
        if vertice >= self.num_vertices or vertice < 0:
            print("Vértice não existe no grafo.")
            return


        self.matriz_adjacencia.pop(vertice)


        for linha in self.matriz_adjacencia:
            linha.pop(vertice)

        self.num_vertices -= 1

    def adicionar_aresta(self, origem, destino):
        """Adiciona uma aresta direcionada do vértice 'origem' para o vértice 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            self.matriz_adjacencia[origem][destino] = 1
        else:
            print("Vértices inválidos para a aresta.")

    def remover_aresta(self, origem, destino):
        """Remove uma aresta direcionada do vértice 'origem' para o vértice 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            self.matriz_adjacencia[origem][destino] = 0
        else:
            print("Vértices inválidos para remover a aresta.")

    def grau_vertice(self, vertice):
        """Calcula o grau de um vértice"""
        if vertice < self.num_vertices:
            grau_saida = sum(self.matriz_adjacencia[vertice])
            grau_entrada = sum([linha[vertice] for linha in self.matriz_adjacencia])
            return grau_saida, grau_entrada
        else:
            print("Vértice inválido.")
            return None, None

    def existe_aresta(self, origem, destino):
        """Verifica se existe uma aresta entre os vértices 'origem' e 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            return self.matriz_adjacencia[origem][destino] == 1
        return False

    def vizinhos(self, vertice):
        """Lista os vizinhos de um vértice"""
        if vertice < self.num_vertices:
            vizinhos = [i for i, existe in enumerate(self.matriz_adjacencia[vertice]) if existe]
            return vizinhos
        else:
            print("Vértice inválido.")
            return []

    def percurso_possivel(self, origem, destino):
        """Verifica se um percurso entre dois vértices é possível """
        if origem >= self.num_vertices or destino >= self.num_vertices:
            print("Vértices inválidos.")
            return False


        visitados = [False] * self.num_vertices
        return self._dfs(origem, destino, visitados)

    def _dfs(self, origem, destino, visitados):

        if origem == destino:
            return True

        visitados[origem] = True

        for i in range(self.num_vertices):
            if self.matriz_adjacencia[origem][i] == 1 and not visitados[i]:
                if self._dfs(i, destino, visitados):
                    return True
        return False

    def mostrar_matriz(self):
        """Exibe a matriz de adjacência"""
        for linha in self.matriz_adjacencia:
            print(linha)


grafo = Grafo()
grafo.inserir_vertice()
grafo.inserir_vertice()
grafo.inserir_vertice()
grafo.inserir_vertice()

grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)

grafo.mostrar_matriz()

print("\nGrau de cada vértice:")
for v in range(grafo.num_vertices):
    grau_saida, grau_entrada = grafo.grau_vertice(v)
    print(f"Vértice {v}: Grau de saída = {grau_saida}, Grau de entrada = {grau_entrada}")

print("\nVerificando se existe aresta de 0 para 2:", grafo.existe_aresta(0, 2))
print("Verificando se existe aresta de 1 para 0:", grafo.existe_aresta(1, 0))

print("\nVizinhos do vértice 1:", grafo.vizinhos(1))

print("\nPercurso de 0 a 3 é possível:", grafo.percurso_possivel(0, 3))
print("Percurso de 3 a 0 é possível:", grafo.percurso_possivel(3, 0))