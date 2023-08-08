"""
The EBNF rules that define the Directed Graph Notation (DGN) are as follows:
<graph> ::= <item> {"\n" <item>}
<item> ::= <nodeblock> | <edgeblock>
<nodeblock> ::= <label> "\n" <attributes>
<edgeblock> ::= <label> ": " <label> "\n" <attributes>
<attributes> ::= <indentation> <attribute> {"\n" <indentation> <attribute>} "\n"
<indentation> ::= " "
<label> ::= <letter> { <letter> }
<letter> ::= any ASCII letter including " "
<attribute> ::= <label> " " <number>
<number> ::= [ "-" ] ( <integer> | <float> )
<integer> ::= <digit> { <digit> }
<float> ::= <digit> { <digit> } "." <digit> { <digit> }
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
"""


with open('source.txt', 'r') as infile:
    lines = infile.readlines()
    print(lines)
    remaining_lines = []
    for line in lines:
        remaining_lines.append(line.strip())
    print(remaining_lines[0][0])

# strip() removes the \n from the end of each line
# split() splits the line into a list of words

# Digit rule
def digit(tokens):
    """
    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    """
    if tokens[0][0] in '0123456789':
        value = int(tokens[0][0])
        tokens.pop(0)
    else:
        raise SyntaxError('Found {}'.format(tokens[0][0]))
    return value

digit(remaining_lines)