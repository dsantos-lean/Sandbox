from task1_dgn_parser_FINAL import *


def dgn_search(start_node, search_attribute, source_graph):
    graph = dgn_parser(source_graph)
    queue = []
    queue.append(start_node)
    visited = []
    step = 1
    # print(graph)
    hello = [key for key in search_attribute.keys()]
    print(hello)
    while queue:
        start_node = queue.pop(0)
        print('dequeue', start_node)

        if start_node not in visited:
            visited.append(start_node)
            print('visiting', start_node)

        print(graph[start_node][hello[0]])

dgn_search('Jack Smith', {'age': 25}, 'parse.pon')
