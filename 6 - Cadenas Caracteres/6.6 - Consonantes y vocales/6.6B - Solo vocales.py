
def soloVocales(string) -> str:
    string = list(string)
    for i, l in enumerate(string):
        if l.isalpha() and l.lower() not in ('a', 'e', 'i', 'o', 'u'):
            del string[i]
    return ''.join(string)
