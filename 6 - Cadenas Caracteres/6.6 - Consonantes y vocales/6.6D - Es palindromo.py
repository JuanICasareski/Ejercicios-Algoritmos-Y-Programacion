
def esPalindromo(string) -> bool:
    string = list(str(string))
    
    for i, l in enumerate(string):
        if not (l.isalpha() or l.isnumeric()):
            del string[i]
    string = ''.join(string).lower()

    return string == string[::-1]
