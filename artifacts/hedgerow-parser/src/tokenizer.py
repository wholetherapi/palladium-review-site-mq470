SEPARATORS = " \t\n\r"

def tokenize(line):
    token = []
    for char in line:
        if char in SEPARATORS:
            if token:
                yield "".join(token)
                token = []
        else:
            token.append(char)
    if token:
        yield "".join(token)

def classify(token):
    if token.startswith("[") and token.endswith("]"):
        return "tag"
    if token.replace(".", "", 1).isdigit():
        return "number"
    return "word"
