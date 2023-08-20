from pyvis.network import Network
from ast import literal_eval


# graph = dgn_filename
file = open('data/basic_test.pon', 'r')
graph = eval(file.read())
file.close()

net = Network(directed=True, select_menu=True, filter_menu=True)

for node in graph:
    net.add_node(node)

for node in graph:
    for edge in graph[node]:
        if ' ' in edge:
            print(edge)
            net.add_edge(node, edge)

net.show_buttons(filter_=['physics'])
net.repulsion(node_distance=500)

net.save_graph('chuchu.html')
