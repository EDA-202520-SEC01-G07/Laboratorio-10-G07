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
      