from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s
from DataStructures.Map import map_linear_probing as m

def dfs(my_graph, source):
    # grafo que almacenará los visitados
    d = m.new_map(2, 0.5)
    visitados = m.new_map(G.size(my_graph),0.7)
    m.put(visitados, source, {"marked": True, "edge_from": None})
    m.put(d, "source", source)
    m.put(d, "visited", visitados)
    dfs_vertex(my_graph, source, d)
    return d

def dfs_vertex(my_graph, vertex_key, dict):
    # Marcar el vértice como visitado
    visitados = m.get(dict, "visited")

    # Obtener la lista de adyacencia del vértice
    adyacentes = m.key_set(G.adjacent(my_graph, vertex_key))

    # Recorrer cada vecino
    for i in range(lt.size(adyacentes)):
        vecino = lt.get_element(adyacentes, i)

        # Si no ha sido visitado
        if not m.contains(visitados, vecino):
            m.put(visitados, vecino, {"marked": True, "edge_from": vertex_key})
            dfs_vertex(my_graph, vecino, dict)  # LLAMADA RECURSIVA

def has_path_to(key_v, visited_map):
    return m.contains(visited_map, key_v)

def path_to(key_v, visited_map):
    path=s.new_stack()
    current_key=key_v
    if not m.contains(visited_map, key_v):
        return None
    else:
        while current_key is not None:
            s.push(path, current_key)
            i =m.get(visited_map, current_key)
            current_key = i["edge_from"]
        return path
    
