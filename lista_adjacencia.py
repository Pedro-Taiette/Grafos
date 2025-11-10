from collections import deque

class Grafo:
    def __init__(self):
        self.lista_adjacencia = []
        self.num_vertices = 0

    def inserir_vertice(self):
        """Adiciona um novo vértice ao grafo"""
        # O novo vértice é simplesmente adicionado no final da lista
        self.lista_adjacencia.append([])
        self.num_vertices += 1

    def remover_vertice(self, vertice):
        """Remove um vértice do grafo"""
        if vertice >= self.num_vertices or vertice < 0:
            print("Vértice não existe no grafo.")
            return

        # 1. Remove o vértice (lista) da lista de adjacência
        self.lista_adjacencia.pop(vertice)
        self.num_vertices -= 1
        
        # 2. Remove todas as referências ao vértice removido (arestas de entrada)
        # E atualiza os índices dos vizinhos que eram maiores que o vértice removido
        for i in range(self.num_vertices):
            nova_lista = []
            for vizinho in self.lista_adjacencia[i]:
                if vizinho != vertice:
                    # Se o índice do vizinho era maior, ele agora deve ser menor
                    nova_lista.append(vizinho if vizinho < vertice else vizinho - 1)
            self.lista_adjacencia[i] = nova_lista

    def adicionar_aresta(self, origem, destino):
        """Adiciona uma aresta direcionada do vértice 'origem' para o vértice 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            if destino not in self.lista_adjacencia[origem]:
                self.lista_adjacencia[origem].append(destino)
        else:
            print("Vértices inválidos para a aresta.")

    def remover_aresta(self, origem, destino):
        """Remove uma aresta direcionada do vértice 'origem' para o vértice 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            if destino in self.lista_adjacencia[origem]:
                self.lista_adjacencia[origem].remove(destino)
        else:
            print("Vértices inválidos para remover a aresta.")

    def grau_vertice(self, vertice):
        """Calcula o grau de um vértice"""
        if vertice < self.num_vertices:
            # Grau de Saída: número de vizinhos (comprimento da lista)
            grau_saida = len(self.lista_adjacencia[vertice])
            
            # Grau de Entrada: número de vezes que 'vertice' aparece como vizinho em outras listas
            grau_entrada = 0
            for i in range(self.num_vertices):
                if vertice in self.lista_adjacencia[i]:
                    grau_entrada += 1
                    
            return grau_saida, grau_entrada
        else:
            print("Vértice inválido.")
            return None, None

    def existe_aresta(self, origem, destino):
        """Verifica se existe uma aresta entre os vértices 'origem' e 'destino'"""
        if origem < self.num_vertices and destino < self.num_vertices:
            return destino in self.lista_adjacencia[origem]
        return False

    def vizinhos(self, vertice):
        """Lista os vizinhos de um vértice"""
        if vertice < self.num_vertices:
            return self.lista_adjacencia[vertice]
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

        # Itera apenas sobre os vizinhos diretos (mais rápido que Matriz de Adjacência)
        for vizinho in self.lista_adjacencia[origem]:
            if not visitados[vizinho]:
                if self._dfs(vizinho, destino, visitados):
                    return True
        return False

    def mostrar_matriz(self):
        """Exibe a lista de adjacência (renomeado para refletir a estrutura)"""
        print("Lista de Adjacência:")
        for i, vizinhos in enumerate(self.lista_adjacencia):
            print(f"Vértice {i}: {vizinhos}")


# --- EXEMPLO DE USO ---

grafo = Grafo()
grafo.inserir_vertice() # 0
grafo.inserir_vertice() # 1
grafo.inserir_vertice() # 2
grafo.inserir_vertice() # 3

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