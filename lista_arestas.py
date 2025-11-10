from collections import deque

class Grafo:

    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo."""
        if vertice not in self.grafo:
            self.grafo[vertice] = {}
            print(f"Vértice '{vertice}' adicionado.")
        else:
            print(f"Vértice '{vertice}' já existe.")

    def remover_vertice(self, vertice):
        """Remove um vértice e todas as arestas conectadas a ele."""
        if vertice not in self.grafo:
            print(f"Erro: Vértice '{vertice}' não encontrado.")
            return

        del self.grafo[vertice]

        for v in self.grafo:
            if vertice in self.grafo[v]:
                del self.grafo[v][vertice]

        print(f"Vértice '{vertice}' e suas arestas removidos.")

    def adicionar_aresta(self, v1, v2, peso=1, direcionado=False):
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)

        self.grafo[v1][v2] = peso
        print(f"Aresta '{v1}' -> '{v2}' (peso: {peso}) adicionada.")

        if not direcionado:
            self.grafo[v2][v1] = peso
            print(f"Aresta '{v2}' -> '{v1}' (peso: {peso}) adicionada (não-direcionado).")

    def remover_aresta(self, v1, v2, direcionado=False):
        if v1 not in self.grafo or v2 not in self.grafo:
            print(f"Erro: Um dos vértices ('{v1}' ou '{v2}') não existe.")
            return

        if v2 in self.grafo[v1]:
            del self.grafo[v1][v2]
            print(f"Aresta '{v1}' -> '{v2}' removida.")

        if not direcionado and v1 in self.grafo[v2]:
            del self.grafo[v2][v1]
            print(f"Aresta '{v2}' -> '{v1}' removida (não-direcionado).")

    def existe_aresta(self, v1, v2):
        if v1 not in self.grafo or v2 not in self.grafo:
            return False

        return v2 in self.grafo[v1]

    def mostrar_grafo(self):
        if not self.grafo:
            print("O grafo está vazio.")
            return

        print("\n--- Estrutura do Grafo (Lista de Adjacência) ---")
        for vertice, vizinhos in self.grafo.items():
            if not vizinhos:
                print(f"{vertice}: {{}}")
            else:
                print(f"{vertice}:")
                for vizinho, peso in vizinhos.items():
                    print(f"  -> {vizinho} (peso: {peso})")
        print("--------------------------------------------------\n")

    def bfs(self, inicio):
        if inicio not in self.grafo:
            print(f"Erro: Vértice de início '{inicio}' não existe.")
            return

        visitados = set()
        fila = deque([inicio])
        ordem_visita = []

        visitados.add(inicio)

        while fila:
            vertice_atual = fila.popleft()
            ordem_visita.append(vertice_atual)

            for vizinho in self.grafo[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        print(f"Percurso BFS a partir de '{inicio}': {ordem_visita}")
        return ordem_visita

    def dfs(self, inicio):
        if inicio not in self.grafo:
            print(f"Erro: Vértice de início '{inicio}' não existe.")
            return

        visitados = set()
        pilha = [inicio]
        ordem_visita = []

        while pilha:
            vertice_atual = pilha.pop()

            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                ordem_visita.append(vertice_atual)

                for vizinho in reversed(list(self.grafo[vertice_atual].keys())):
                    if vizinho not in visitados:
                        pilha.append(vizinho)

        print(f"Percurso DFS a partir de '{inicio}': {ordem_visita}")
        return ordem_visita


# --- EXEMPLO DE USO ---

g = Grafo()

g.adicionar_aresta('A', 'B', peso=5)
g.adicionar_aresta('A', 'C', peso=3)
g.adicionar_aresta('B', 'C', peso=2)
g.adicionar_aresta('B', 'D', peso=8)
g.adicionar_aresta('C', 'E', peso=7)
g.adicionar_vertice('F')

g.mostrar_grafo()

print(f"Existe aresta A-B? {g.existe_aresta('A', 'B')}") # True
print(f"Existe aresta A-D? {g.existe_aresta('A', 'D')}") # False

g.bfs('A')
g.dfs('A')

print("\n--- Modificando o Grafo ---")
g.remover_aresta('A', 'C')
g.remover_vertice('D')

g.mostrar_grafo()