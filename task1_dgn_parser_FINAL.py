import string

# def dgn_parser(filename):
with open('source.txt') as file:
    lines = file.readlines()
    # lines.copy()


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
        line = line.strip()
    else:
        line = lines
    common_letters = set(line) & set(string.ascii_letters)

    if len(common_letters) == 0:
        raise ValueError("invalid label")
    return line


def parse_attribute(lines):
    # <attribute> ::= <label> : <number>
    line = lines.pop(0)
    line = line.strip()
    parts = line.rsplit(" ", 1)
    attribute_label = parse_label(parts[0])
    number = parse_number(parts[1])
    # result = " ".join([attribute_label, str(number)])
    result = attribute_label, str(number)
    return result


def parse_attributes(lines):
    # <attributes> ::= <indentation> <attribute> {"\n" <indentation> <attribute>} "\n"
    attributes = {}
    while lines[0] != '\n':
        attribute = [parse_attribute(lines)]
        attributes.update(attribute)
    return attributes

def parse_node(lines):
    graph = {}
    label = parse_label(lines)
    attributes = parse_attributes(lines)
    graph[label] = {}
    graph[label] = attributes
    return graph



# print(f'This should be Jack Smith, result: {parse_label(lines)}')
# print(parse_attribute(lines))
# print(parse_label(lines))
# print(parse_attribute(lines))
# print(parse_attributes(lines))
print(parse_node(lines))
# dgn_parser('source.txt')