from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as ml
def new_graph(order):
    graph= {
        "vertices" :ml.new_map(order, 0.5, prime=109345121), 
        "num_edges":0
    }
    return graph
    
def insert_vertex(my_graph, key_u, info_u):
    vertex = {
        "key": key_u,
        "info": info_u,
        "adyacentes": lt.new_list()
    }
    ml.put(my_graph["vertices"], key_u, vertex)
    return my_graph
    

def add_edge (my_graph, key_u, key_v, weight=1.0):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None or vertex_v is None:
        raise Exception("El vertice u no existe")
    vertex_v = ml.get(my_graph["vertices"], key_v)
    if vertex_v is None:
        raise Exception("El vertice v no existe")
    lt.add_last(vertex_u["adyacentes"], (key_v, weight))
    my_graph["num_edges"] += 1
    return my_graph

def contains_vertex(my_graph, key_u):
    return ml.contains(my_graph["vertices"], key_u)

def order(my_graph):
    return ml.size(my_graph["vertices"])

def size(my_graph):
    return my_graph["num_edges"]

def degree(my_graph, key_u):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    return lt.size(vertex_u["adyacentes"])

def adjacent(my_graph, key_u):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    return vertex_u["adyacentes"]

def vertices (my_graph):
    keys = ml.key_set(my_graph["vertices"])
    return keys

def edges_vertex(my_graph, key_u):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    return vertex_u["adyacentes"]

def get_vertex(my_graph, key_u):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    return vertex_u

def update_vertex_info(my_graph, key_u, new_info):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    vertex_u["info"] = new_info
    ml.put(my_graph["vertices"], key_u, vertex_u)
    return my_graph

def get_vertex_information(my_graph, key_u):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    return vertex_u["info"]

