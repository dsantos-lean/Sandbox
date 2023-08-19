import string


graph = {}


def dgn_parser(filename):
    with open(filename) as file:
        lines = file.readlines()
        graph = item(lines)
    print(graph)


def parse_number(line):
    # <number> ::= [ "-" ] ( <integer> | <float> )
    # a number optionally starts with a -
    # and then is followed by an int or a float

    # line = lines.pop(0)  # grab the next line and consume it
    # line = line.strip()

    is_negative = False
    if line[0] == "-":
        is_negative = True
        line = line[1:]

    # compute the number

    # can I tell if the line contains only digits?
    if line.isdigit():
        # the line must be an integer!
        number = int(line)
    else:
        # assume that it is a float??? :)
        number = float(line)

    if is_negative:
        return -1 * number
    return number


def parse_label(lines):
    # <label> ::= <letter> { <letter> }
    if isinstance(lines, list):
        line = lines.pop(0)
        if line == '\n':
            line = parse_label(lines)
        line = line.strip()
        common_letters = set(line) & set(string.ascii_letters)
        if len(common_letters) == 0:
            raise ValueError("invalid label")
    else:
        line = lines

    return line


def parse_attribute(lines):
    # <attribute> ::= <label> : <number>
    line = lines.pop(0)
    while line != '\n':
        line = line.strip()
        parts = line.rsplit(" ", 1)
        attribute_label = parse_label(parts[0])
        number = parse_number(parts[1])
        # result = " ".join([attribute_label, str(number)])
        result = attribute_label, number  # str(number)
        return result


def parse_attributes(lines):
    # <attributes> ::= <indentation> <attribute> {"\n" <indentation> <attribute>} "\n"
    attributes = {}
    while len(lines) > 0:
        if lines[0] == '\n':
            return attributes
        attribute = [parse_attribute(lines)]
        if None not in attribute:
            attributes.update(attribute)
    return attributes
    # if len(attributes) == 0:
    #     del attributes


def parse_node(label, lines, graph):
    # print(f'Hello {graph}')
    while len(lines) > 0:
        # label = parse_label(lines)
        attributes = parse_attributes(lines)
        graph[label] = {}
        graph[label].update(attributes)
        item(lines)
    return graph


def parse_edge(label, lines, graph):
    inner_graph = {}
    graph_keys = [keys for keys in graph.keys()]
    parts = label.split(": ", 1)
    node_label = parts[0]
    edge_label = parts[1]
    if node_label in graph_keys:
        attributes = parse_attributes(lines)
        inner_graph[edge_label] = {}
        inner_graph[edge_label].update(attributes)
        graph[node_label].update(inner_graph)
    return graph


def item(lines):
    label = parse_label(lines)
    if ':' in label:
        result = parse_edge(label, lines, graph)
    else:
        result = parse_node(label, lines, graph)
    return result


# Testing the different functions
# print(f'This should be Jack Smith, result: {parse_label(lines)}')
# print(parse_attribute(lines))
# print(parse_label(lines))
# print(parse_attribute(lines))
# print(parse_attributes(lines))
# print(parse_node(lines))
# print(parse_node(lines, graph))
# parse_edge(lines)


dgn_parser('source.txt')