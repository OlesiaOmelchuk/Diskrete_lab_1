import matplotlib.pyplot as plt
import time
from prim import gnp_random_connected_graph, prim
from kruskal import kruskal


num_of_nodes = [20, 50, 100, 200, 250, 400, 500, 700]
iterations_num = 15
completeness = 1

prim_time_execution = []
kruskal_time_execution = []

for nodes in num_of_nodes:
    graph = gnp_random_connected_graph(nodes, completeness)

    prim_all = []
    for i in range(iterations_num):
        start = time.time()
        prim(graph)
        end = time.time()
        time_taken = end-start
        prim_all.append(time_taken)
    prim_min_time = min(prim_all)
    prim_time_execution.append(round(prim_min_time, 5))

    kruskal_all = []
    for i in range(iterations_num):
        start = time.time()
        kruskal(graph)
        end = time.time()
        time_taken = end-start
        kruskal_all.append(time_taken)
    kruskal_min_time = min(kruskal_all)
    kruskal_time_execution.append(round(kruskal_min_time, 5))

plt.plot(num_of_nodes, prim_time_execution, label="Prim's algorithm")
plt.plot(num_of_nodes, kruskal_time_execution, label="Kruskal's algorithm")

plt.xlabel('number of nodes')
plt.ylabel('time of execution, seconds')
plt.title('Comparison')
plt.legend()

plt.show()
