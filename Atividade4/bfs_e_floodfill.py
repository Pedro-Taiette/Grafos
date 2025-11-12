# implemente uma busca em largura em cima de uma das implementações de grafos que voce desejar

from dataclasses import dataclass, field
from collections import deque

@dataclass
class DataPair:
    vertex : int = field(default_factory=int)
    path : list[str] = field(default_factory=list[str])

@dataclass
class Grafo:
    g: set = field(default_factory=set) 
    adjacency_list: dict[str, list[str]] = field(default_factory=dict)
    num_vertex: int = 0

    def bfs_floodfill(self, starting_vertex : str, desired_vertex : str):
        # paths : dict[list[str]] = {starting_vertex : starting_vertex}
        queue : list[DataPair]= [DataPair(starting_vertex, [starting_vertex])]
        
        visited = []

        while queue != []:
            pick = queue.pop(0)
            visited.append(pick.vertex)
            neighbours = self._get_neighbours(pick.vertex)
            
            for x in neighbours:
                if x in visited:
                    continue

                queue.append(DataPair(x, pick.path + [x]))

                if x == desired_vertex:
                    return queue[-1].path
        
        return "path not found"

    def bfs(self, starting_vertex : str):
        """
        1. Inserir o vértice inicial na fila
        2. Iniciar a lista de visitados vazia
        3. Enquanto a fila não estiver vazia:
            a. Retirar o primeiro vertice da fila
            b. Marcar vértice como visitado
            c. Obter os vizinhos do vértice
            d. Para cada vizinho:
                  i. Verificar se o vizinho já não está na fila
                 ii. Verificar se o vizinho já não foi visitado
                iii. Adicionar o vizinho na Fila
        4. Retornar visitados
        """
        queue = [starting_vertex] # vertice inicial
        visited = []

        while queue != []:
            pick = queue.pop(0)
            visited.append(pick)
            neighbours = self._get_neighbours(pick)

            for x in neighbours:
                if x in visited:
                    continue
                queue.append(x)
        
        return visited


    def _get_neighbours(self, vertex: str) -> list[str]:
        return self.adjacency_list[vertex]
    
    def add_vertex(self, vertex : str) -> bool:
        if vertex in self.adjacency_list.keys():
            return False
        
        self.adjacency_list[vertex] = []
        self.num_vertex += 1
    
    def add_path(self, v_from, v_to):
        self.adjacency_list[v_from].append(v_to)


g = Grafo()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_path("A", "C")
g.add_path("A", "D")
g.add_path("D", "E")

print(f" BFS A: {g.bfs("A")}")
print(f"A -> B: {g.bfs_floodfill("A", "B")}")
print(f"A -> E: {g.bfs_floodfill("A", "E")}")
