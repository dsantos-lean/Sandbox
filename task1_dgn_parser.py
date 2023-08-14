import string


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


def parse_attribute(lines, node_label, graph):
    # <attribute> ::= <label> " " <number>
    # check for a "label", then a space, then a number
    line = lines.pop(0)  # grab the next line and consume it
    while not line.startswith('\n') and len(lines) != 0:
        line = line.strip()
        tokens = line.rsplit(" ", 1)  # split from the right, spit only 1 time

        label = tokens[0]

        common_letters = set(label) & set(string.ascii_letters)

        if len(common_letters) == 0:
            raise ValueError("invalid label")

        number = parse_number(tokens[1])

        # print(label, number)

        # attribute_dict = {label: number}
        graph[node_label][label] = number
        line = lines.pop(0)


def parse_label(lines):
    line = lines.pop(0)  # grab the next line and consume it
    line = line.strip()
    if line.isascii():
        return line
    else:
        raise ValueError('Invalid Label')


# can we get the file as a list of lines of text?


def dgn_parser(filename):
    with open(filename) as file:
        lines = file.readlines()
        # print(lines)
        #
        # for line in lines:
        #     print(line)

        # prototype graph

        graph = {}
        while lines:
            node_label = parse_label(lines)
            graph[node_label] = {}
            parse_attribute(lines, node_label, graph)

        # graph["Jack Smith"] = {}

        # print(parse_number(lines))  # DONE!
        # parse_attribute(lines, "Jack Smith", graph)  # DONE!

        return graph

print(dgn_parser('basic_test.dgn'))
