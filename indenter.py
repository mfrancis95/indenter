from re import sub

def indent(file, spaces, to):
    spaces = "^(" + " " * spaces + r")(?=\S)"
    to = " " * to
    for line in map(lambda line: sub(spaces, to, line), file):
        yield line
