import math as math
from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Map import map_linear_probing as ml
from DataStructures.Graph import dijsktra_structure as dj
def bfs(my_graph, source):
    visited_map = ml.new_map(num_elements=G.order(my_graph), load_factor=0.7, prime=109345121)
    ml.put(visited_map, source, {"edge_from": None,"dist_to": 0})
    bfs_vertex(my_graph, source, visited_map)
    return visited_map


def bfs_vertex(my_graph, source, visited_map):
    cola = q.new_queue()
    q.enqueue(cola, source)

    while not q.is_empty(cola):
        v = q.dequeue(cola)
        adj = G.adjacent(my_graph, v) #Es un mapa
        lista = adj["table"]
        for i in range(lt.size(lista)):
            e = lt.get_element(lista, i)
            if e is not None:
                if e is None or e["key"] is None:
                    continue
                w = e["key"]
                if G.contains_vertex(my_graph, w):
                    elem = ml.get(visited_map, w)
                    if elem is None:
                        info = ml.get(visited_map, v)
                        ml.put(visited_map, w, {"edge_from": v, "dist_to": info["dist_to"] + 1})
                        q.enqueue(cola, w)
    return visited_map
        

def has_path_to(key_v, visited_map):
    return ml.contains(visited_map, key_v)

def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None
    else:
        stack=s.new_stack()
        current_key=key_v
        while current_key is not None:
            s.push(stack, current_key)
            info = ml.get(visited_map, current_key)
            current_key= info["edge_from"]
        return stack
    
#De la presentación
def init_structure(graph, source):
    djk = dj.new_dijsktra_structure(source, G.order(graph))
    vertices = G.vertices(graph)
    for i in range(lt.size(vertices)):
        elem = lt.get_element(vertices, i)
        ml.put(djk["visited"], elem, {"marked": False, "edge_from": None, "dist_to": math.inf})
    ml.put(djk["visited"], source, {"marked": False, "edge_from": None, "dist_to": 0})
    pq.insert(djk["pq"], source, 0.0)
    return djk
    
def dijkstra(graph, source):
    if not G.contains_vertex(graph,source):
        return None
    else:
        djk = init_structure(graph, source)
        pila = djk["pq"]
        marked = djk["visited"]
        
        while not pq.is_empty(pila):
            v_m = pq.remove(pila)
            marcado = ml.get(marked, v_m)["value"]
            dist_vm = marcado["dist_to"]
            ml.put(marked, v_m, {"marked": True, "edge_from": marcado["edge_from"], "dist_to": dist_vm})
            
            adj = G.adjacent(graph, v_m)
            llaves = ml.key_set(adj)
            for i in range(lt.size(llaves)):
                elem = lt.get_element(llaves, i)
                peso = ml.get(adj, elem)
                mark = ml.get(marked, elem) #me da el value directamente
                if mark is None:
                    continue
                if mark["marked"] is False:
                    costo = peso + dist_vm
                    if costo < mark["dist_to"]:
                        mark["dist_to"] = costo
                        mark["edge_from"] = v_m
                        ml.put(marked, elem, {"marked": False, "edge_from": v_m, "dist_to": mark["dist_to"]})
                        pq.insert(pila, elem, costo)
        return djk
    
def dist_to(key_v, aux):
    nodo = ml.get(aux["visited"], key_v)
    return (nodo["dist_to"])
        
def has_path_to(key_v, aux):
    elem = ml.contains(aux["visited"], key_v)
    if elem["dist_to"] != math.inf:
        return True
    return False

def path_to(key_v, aux):
    nodo = ml.get(aux["visited"], key_v)
    if not has_path_to(key_v, aux):
        return None
    else:
        stack = s.new_stack()
        s.push(stack, nodo)
        while nodo != aux["source"]:
            visitado = nodo["edge_from"]
            s.push(stack, visitado)
            nodo = visitado["edge_from"]
        return stack