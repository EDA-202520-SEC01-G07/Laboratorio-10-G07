from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s
from DataStructures.Map import map_linear_probing as ml
def bfs(my_graph, source):
    visited_map = ml.new_map(num_elements=G.order(my_graph), load_factor=0.5, prime=109345121)
    ml.put(visited_map, source, {"edge_from": None,"dist_to": 0})
    bfs_vertex(my_graph, source, visited_map)
    return visited_map


def bfs_vertex(my_graph, source, visited_map):
    cola = q.new_queue()
    q.enqueue(cola, source)

    while not q.is_empty(cola):
        v = q.dequeue(cola)
        adj = G.adjacent(my_graph, v)
        for i in range(lt.size(adj)):
            w = lt.get_element(adj, i)
            if not ml.contains(visited_map, w):
                info_v = ml.get(visited_map, v)
                ml.put(visited_map, w, {"edge_from": v,"dist_to": info_v["dist_to"] + 1})
                q.enqueue(cola, w)
    return visited_map
        

def has_path_to(key_v, visited_map):
    return G.contains_vertex(visited_map, key_v)

def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None
    else:
        stack=s.new_stack()
        current_key=key_v
        while current_key is not None:
            s.push(stack, current_key)
            current_key=visited_map[current_key]
        return stack
           
        







      
