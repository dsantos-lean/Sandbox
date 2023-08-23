# from task1_dgn_parser_FINAL import *


def dgn_search(start_node, target_attributes, source_graph):
    # graph = dgn_parser(source_graph)
    graph_keys = [key for key in source_graph]
    queue = [start_node]
    visited = []
    fresh_graph = {}
    step = 1
    while queue:
        person = queue.pop(0)
        print('dequeue', person)

        if person not in visited:
            visited.append(person)
            print('visiting', person)

        for neighbor in graph[person]:
            if neighbor in graph_keys and neighbor not in visited:
                print('enqueue', neighbor)
                queue.append(neighbor)
                if target_attributes.intersection(graph[neighbor].keys()) == target_attributes:  # Check if the neighbor's attributes are the target attributes
                    similar_node = {}
                    for item in graph_keys:
                        if item in graph[neighbor]:
                            graph[neighbor].pop(item)  # Remove the edge
                    similar_node[neighbor] = graph[neighbor]
                    fresh_graph.update(similar_node)

        print(f'step {step} queue: {queue} visited: {visited}')
        step += 1

    print(f'Fresh Graph {fresh_graph}')


# graph = {'Jack Smith': {'age': 2, 'income': 2,
#                         'Jill Smith': {'posts per day': 10, 'post length': 120, 'post sentiment': 0.5}},
#          'Jill Smith': {'age': 4, 'income': 4}}
graph = {'Jack Smith': {'age': 32, 'income': 23,
                        'Jill Smith': {'posts per day': 10, 'post length': 120, 'post sentiment': 0.5}, 'Lean Delos Santos': {'posts per day': 5, 'post length': 10, 'post sentiment': 1.5}},
         'Jill Smith': {'income': 42, 'Alan Turing': {'posts per day': 76, 'post length': 60, 'post sentiment': 2.5}}, 'Lean Delos Santos': {'age': 20, 'income': 40}, 'Alan Turing': {'age': 80, 'income': 1600, 'Jack Smith': {'posts per day': 2, 'post length': 50, 'post sentiment': 2}}}
dgn_search('Jack Smith', {'age', 'income'}, graph)
