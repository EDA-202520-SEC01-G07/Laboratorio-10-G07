from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s

def dfs(my_graph, source):
    visitados= G.new_graph(order=0)
    dfs_vertex(my_graph, source, visitados)
    return visitados

def dfs(my_graph, source):
    # grafo que almacenará los visitados
    visitados = G.new_graph(order=0)
    dfs_vertex(my_graph, source, visitados)
    return visitados


def dfs_vertex(my_graph, vertex_key, visitados):
    # Marcar el vértice como visitado
    G.insert_vertex(visitados, vertex_key, None)

    # Obtener la lista de adyacencia del vértice
    adyacentes = G.adjacent(my_graph, vertex_key)

    # Recorrer cada vecino
    for i in range(lt.size(adyacentes)):
        vecino = lt.get_element(adyacentes, i+1)[0]

        # Si no ha sido visitado
        if not G.contains_vertex(visitados["vertices"], vecino):
            dfs_vertex(my_graph, vecino, visitados)  # LLAMADA RECURSIVA

def has_path_to(key_v, visited_map):
    return G.contains_vertex(visited_map, key_v)

def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None
    else:
        path=s.new_stack()
        current_key=key_v
        while current_key is not None:
            s.push(path, current_key)
            current_key=visited_map[current_key]
        return path
    
