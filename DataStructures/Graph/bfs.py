from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as s
def bfs(my_graph,source):
    visitados = G.new_graph(order=0)
    edge_from= G.new_graph(order=0)
    cola=q.new_queue()
    visitados[source]=True
    q.enqueue(cola,source)
    while not q.is_empty(cola):
        v=q.dequeue(cola)
        adj= q(my_graph,v)
        for i in range(lt.size(adj)):
            if not visitados[i]:
                visitados[adj[i]]=True
                q.enqueue(cola,adj[i])
                edge_from[adj[i]]=v
    return visitados, edge_from

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
           