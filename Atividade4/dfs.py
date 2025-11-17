from dataclasses import dataclass, field

@dataclass
class Grafo:
    g: set = field(default_factory=set) 
    adjacency_list: dict[str, list[str]] = field(default_factory=dict)
    num_vertex: int = 0
    
    def dfs(self, starting_vertex : str):
        heap = [starting_vertex]
        visited = []

        while heap != []:
            pick = heap.pop()
            visited.append(pick)
            neighbours = self._get_neighbours(pick)
            neighbours.sort(reverse=False)

            for x in neighbours:
                if x in visited or x in heap:
                    continue

                heap.append(x)
            
        return visited

    def bfs_com_valor_altearado_de_pop(self, starting_vertex : str):
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
            pick = queue.pop()
            visited.append(pick)
            neighbours = self._get_neighbours(pick)

            for x in neighbours:
                if x in visited or x in queue:
                    continue
                queue.append(x)
        
        return visited

    def _get_neighbours(self, vertex: str) -> list[str]:
        return self.adjacency_list[vertex]
    
    def add_vertexes(self, vertexes : list[str]):
        for v in vertexes:
            self.add_vertex(v)

    def add_vertex(self, vertex : str) -> bool:
        if vertex in self.adjacency_list.keys():
            return False
        
        self.adjacency_list[vertex] = []
        self.num_vertex += 1
    
    def add_path(self, v_from, v_to):
        self.adjacency_list[v_from].append(v_to)

    def add_path_unordered(self, v_from, v_to):
        self.adjacency_list[v_from].append(v_to)
        self.adjacency_list[v_to].append(v_from)


g = Grafo()
g.add_vertexes(["V1", "V2", "V3",  "V5", "V4","V6", "V7", "V8"])
g.add_path_unordered("V1", "V2")
g.add_path_unordered("V1", "V3")
g.add_path_unordered("V1", "V6")
g.add_path_unordered("V2", "V4")
g.add_path_unordered("V2", "V6")
g.add_path_unordered("V2", "V7")
g.add_path_unordered("V4", "V5")
g.add_path_unordered("V5", "V6")
g.add_path_unordered("V5", "V8")
g.add_path_unordered("V6", "V7")
g.add_path_unordered("V7", "V8")

print(f"dfs: {g.dfs('V1')}")
print(f"bfs: {g.bfs('V1')}")
