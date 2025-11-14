from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as ml
def new_graph(order):
    graph = ml.new_map(order, 0.5, prime=109345121)
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

