import random

class Grafo:
    def __init__(self, es_dirigido=False, vertices_init=[]):
        self.vertices = {}
        self.es_dirigido = es_dirigido
        
        for v in vertices_init:
            self.agregar_vertice(v)
    
    def agregar_vertice(self, v):
        """Agrega un vértice al grafo - O(1)"""
        if v not in self.vertices:
            self.vertices[v] = {}
    
    def borrar_vertice(self, v):
        """Elimina un vértice y todas sus aristas incidentes - O(grado(v)) en no dirigido, O(V) en dirigido"""
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe en el grafo")
        
        # Eliminar aristas salientes
        for w in list(self.vertices[v].keys()):
            self.borrar_arista(v, w)
        
        # Eliminar aristas entrantes (solo necesario en grafos dirigidos)
        if self.es_dirigido:
            for u in self.vertices:
                if v in self.vertices[u]:
                    del self.vertices[u][v]
        
        del self.vertices[v]
    
    def agregar_arista(self, v, w, peso=1):
        """Agrega una arista al grafo - O(1)"""
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("Uno o ambos vértices no existen")
        
        self.vertices[v][w] = peso
        if not self.es_dirigido and v != w:
            self.vertices[w][v] = peso
    
    def borrar_arista(self, v, w):
        """Elimina una arista del grafo - O(1)"""
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("Uno o ambos vértices no existen")
        
        if w not in self.vertices[v]:
            raise ValueError(f"La arista ({v}, {w}) no existe")
        
        del self.vertices[v][w]
        if not self.es_dirigido and w in self.vertices and v in self.vertices[w]:
            del self.vertices[w][v]
    
    def estan_unidos(self, v, w):
        """Verifica si dos vértices están unidos por una arista - O(1)"""
        if v not in self.vertices or w not in self.vertices:
            return False
        return w in self.vertices[v]
    
    def peso_arista(self, v, w):
        """Obtiene el peso de una arista - O(1)"""
        if not self.estan_unidos(v, w):
            raise ValueError(f"La arista ({v}, {w}) no existe")
        return self.vertices[v][w]
    
    def obtener_vertices(self):
        """Devuelve una lista con todos los vértices - O(V)"""
        return list(self.vertices.keys())
    
    def vertice_aleatorio(self):
        """Devuelve un vértice aleatorio - O(1)"""
        if not self.vertices:
            return None
        return random.choice(list(self.vertices.keys()))
    
    def adyacentes(self, v):
        """Devuelve los vértices adyacentes a un vértice - O(1) para obtener, O(grado(v)) para copiar"""
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe en el grafo")
        return list(self.vertices[v].keys())
    
    def __str__(self):
        """Representación de cadena del grafo - O(V + E)"""
        s = "Vertices: " + str(self.obtener_vertices()) + "\n"
        s += "Aristas:\n"
        
        if self.es_dirigido:
            for v in self.vertices:
                for w, peso in self.vertices[v].items():
                    s += f"  ({v} -> {w}): {peso}\n"
        else:
            printed = set()
            for v in self.vertices:
                for w, peso in self.vertices[v].items():
                    # Evitar duplicados en grafos no dirigidos
                    if (w, v) not in printed:
                        s += f"  ({v} <-> {w}): {peso}\n"
                        printed.add((v, w))
        return s