from dataclasses import dataclass, field

@dataclass
class Grafo:
    g: set = field(default_factory=set)          # conjunto de vértices
    arestas: list[tuple[str, str]] = field(default_factory=list)  # lista de arestas (origem, destino)
    num_vertices: int = 0

    def inserir_vertice(self, vert: str) -> str:
        """Insere um vértice no grafo"""
        if vert in self.g:
            return f"Vértice '{vert}' já existe."
        self.g.add(vert)
        self.num_vertices += 1
        return f"Vértice '{vert}' adicionado com sucesso."

    def remover_vertice(self, vert: str) -> str:
        """Remove um vértice e suas conexões"""
        if vert not in self.g:
            return f"Vértice '{vert}' não existe."
        self.g.remove(vert)
        self.num_vertices -= 1
        # Remove todas as arestas que contêm esse vértice
        self.arestas = [(a, b) for (a, b) in self.arestas if a != vert and b != vert]
        return f"Vértice '{vert}' removido com sucesso."

    def inserir_aresta(self, vert_a: str, vert_b: str, directed: bool = False) -> str:
        """Insere uma aresta entre dois vértices"""
        if vert_a not in self.g or vert_b not in self.g:
            return "Um ou ambos os vértices não existem."

        if (vert_a, vert_b) not in self.arestas:
            self.arestas.append((vert_a, vert_b))
        if not directed and (vert_b, vert_a) not in self.arestas:
            self.arestas.append((vert_b, vert_a))
        return f"Aresta entre '{vert_a}' e '{vert_b}' adicionada."

    def remover_aresta(self, vert_a: str, vert_b: str, directed: bool = False) -> str:
        """Remove uma aresta entre dois vértices"""
        if vert_a not in self.g or vert_b not in self.g:
            return "Um ou ambos os vértices não existem."

        if (vert_a, vert_b) in self.arestas:
            self.arestas.remove((vert_a, vert_b))
        if not directed and (vert_b, vert_a) in self.arestas:
            self.arestas.remove((vert_b, vert_a))
        return f"Aresta entre '{vert_a}' e '{vert_b}' removida."

    def grau_vertices(self) -> dict:
        """Calcula o grau de cada vértice"""
        graus = {v: 0 for v in self.g}
        for (a, b) in self.arestas:
            if a in graus:
                graus[a] += 1
        return graus

    def existe_aresta(self, vert_a: str, vert_b: str) -> bool:
        """Verifica se há uma aresta entre dois vértices"""
        return (vert_a, vert_b) in self.arestas

    def vizinhos(self, vert: str) -> list:
        """Lista os vizinhos de um vértice"""
        if vert not in self.g:
            return []
        return [b for (a, b) in self.arestas if a == vert]

    def percurso_possivel(self, caminho: list[str]) -> bool:
        """Verifica se um percurso é possível no grafo"""
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i + 1]):
                return False
        return True

    def exibir_arestas(self):
        """Mostra a lista de arestas"""
        print("Lista de Arestas:")
        for (a, b) in self.arestas:
            print(f"{a} -> {b}")
        if not self.arestas:
            print("(nenhuma aresta)")

g = Grafo()
print(g.inserir_vertice("A"))
print(g.inserir_vertice("B"))
print(g.inserir_vertice("C"))
print(g.inserir_aresta("A", "B"))
print(g.inserir_aresta("B", "C"))
g.exibir_arestas()
print("Grau dos vértices:", g.grau_vertices())
print("Vizinhos de B:", g.vizinhos("B"))
print("Percurso possível A -> B -> C:", g.percurso_possivel(["A", "B", "C"]))
