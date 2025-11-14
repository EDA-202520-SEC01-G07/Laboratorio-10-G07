from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as ml
def new_graph(order):
    """
    Crea un grafo dirigido.
    order: Numero de vertices del grafo
    """
    graph = ml.new_map(order, 0.5, prime=109345121)
