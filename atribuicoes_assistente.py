import csv
import heapq

class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
        self.adj[u].append((v, float(peso)))
        self.adj[v].append((u, float(peso)))

    def dijkstra(self, inicio):
        if inicio not in self.adj:
            return {}, {}
        dist = {no: float('inf') for no in self.adj}
        dist[inicio] = 0
        pq = [(0, inicio)]
        caminho = {no: [] for no in self.adj}
        caminho[inicio] = [inicio]

        while pq:
            d, atual = heapq.heappop(pq)
            if d > dist[atual]:
                continue
            for vizinho, peso in self.adj.get(atual, []):
                nova_dist = dist[atual] + peso
                if nova_dist < dist.get(vizinho, float('inf')):
                    dist[vizinho] = nova_dist
                    caminho[vizinho] = caminho[atual] + [vizinho]
                    heapq.heappush(pq, (nova_dist, vizinho))
        return dist, caminho

def carregar_grafo(nome_arquivo):
    grafo = Grafo()
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:
                    u, v, p = row[0].strip(), row[1].strip(), row[2].strip()
                    grafo.adicionar_aresta(u, v, p)
    except Exception:
        pass
    return grafo