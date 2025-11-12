from dataclasses import dataclass, field

@dataclass
class Grafo:
    g: set = field(default_factory=set)
    matriz_adjacencia: list[list[int]] = field(default_factory=list)
    num_vertices: int = 0

    def inserir_vertice(self, vert: str) -> str:
        """Insere um vértice no grafo"""
        if vert in self.g:
            return f"Vértice '{vert}' já existe."
        self.g.add(vert)
        self.num_vertices += 1
        # Atualiza matriz de adjacência
        for linha in self.matriz_adjacencia:
            linha.append(0)
        self.matriz_adjacencia.append([0] * self.num_vertices)
        return f"Vértice '{vert}' adicionado com sucesso."

    def remover_vertice(self, vert: str) -> str:
        """Remove um vértice e suas conexões"""
        if vert not in self.g:
            return f"Vértice '{vert}' não existe."
        idx = list(self.g).index(vert)
        self.g.remove(vert)
        self.num_vertices -= 1
        self.matriz_adjacencia.pop(idx)
        for linha in self.matriz_adjacencia:
            linha.pop(idx)
        return f"Vértice '{vert}' removido com sucesso."

    def inserir_aresta(self, vert_a: str, vert_b: str, directed: bool = False) -> str:
        """Insere uma aresta entre dois vértices"""
        if vert_a not in self.g or vert_b not in self.g:
            return "Um ou ambos os vértices não existem."
        idx_a = list(self.g).index(vert_a)
        idx_b = list(self.g).index(vert_b)
        self.matriz_adjacencia[idx_a][idx_b] = 1
        if not directed:
            self.matriz_adjacencia[idx_b][idx_a] = 1
        return f"Aresta entre '{vert_a}' e '{vert_b}' adicionada."

    def remover_aresta(self, vert_a: str, vert_b: str, directed: bool = False) -> str:
        """Remove uma aresta entre dois vértices"""
        if vert_a not in self.g or vert_b not in self.g:
            return "Um ou ambos os vértices não existem."
        idx_a = list(self.g).index(vert_a)
        idx_b = list(self.g).index(vert_b)
        self.matriz_adjacencia[idx_a][idx_b] = 0
        if not directed:
            self.matriz_adjacencia[idx_b][idx_a] = 0
        return f"Aresta entre '{vert_a}' e '{vert_b}' removida."

    def grau_vertices(self) -> dict:
        """Calcula o grau de cada vértice"""
        vertices = list(self.g)
        graus = {}
        for i, vert in enumerate(vertices):
            grau = sum(self.matriz_adjacencia[i])
            graus[vert] = grau
        return graus

    def existe_aresta(self, vert_a: str, vert_b: str) -> bool:
        """Verifica se há uma aresta entre dois vértices"""
        if vert_a not in self.g or vert_b not in self.g:
            return False
        idx_a = list(self.g).index(vert_a)
        idx_b = list(self.g).index(vert_b)
        return self.matriz_adjacencia[idx_a][idx_b] == 1

    def vizinhos(self, vert: str) -> list:
        """Lista os vizinhos de um vértice"""
        if vert not in self.g:
            return []
        idx = list(self.g).index(vert)
        vertices = list(self.g)
        return [vertices[i] for i, val in enumerate(self.matriz_adjacencia[idx]) if val == 1]

    def percurso_possivel(self, caminho: list[str]) -> bool:
        """Verifica se um percurso é possível no grafo"""
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i + 1]):
                return False
        return True

    def exibir_matriz(self):
        """Mostra a matriz de adjacência"""
        print("Matriz de Adjacência:")
        g = list(self.g)
        print(f"    {"  ".join(g)}")
        for index, linha in enumerate(self.matriz_adjacencia):
            print(f"{g[index]}: {linha}")


g = Grafo()
print(g.inserir_vertice("A"))
print(g.inserir_vertice("B"))
print(g.inserir_vertice("C"))
print(g.inserir_aresta("A", "B"))
print(g.inserir_aresta("B", "C"))
g.exibir_matriz()
print("Grau dos vértices:", g.grau_vertices())
print("Vizinhos de B:", g.vizinhos("B"))
print("Percurso possível A → B → C:", g.percurso_possivel(["A", "B", "C"]))