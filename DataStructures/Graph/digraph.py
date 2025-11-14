from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as ml
def new_graph(order):
    graph = { "vertices"=ml.new_map(order, 0.5, prime=109345121),
             "num_edges"=0}
    return graph
    
def insert_vertex(my_graph, key_u, info_u):
    """
    Inserta un vertice en el grafo dirigido.
    my_graph: Grafo dirigido
    key_u: Llave del vertice
    info_u: Informacion del vertice
    """
    ml.put(my_graph["vertices"], key_u, info_u)
    my_graph["order"] += 1
    return my_graph

def add_edge (my_graph, key_u, key_v, weight=1.0):
    vertex_u = ml.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    vertex_v = ml.get(my_graph["vertices"], key_v)
    if vertex_v is None:
        raise Exception("El vertice u no existe")
    adjacency_list = vertex_u["adjacency"]
    lt.add_last(adjacency_list, (key_v, weight))
    my_graph["size"] += 1
    return my_graph