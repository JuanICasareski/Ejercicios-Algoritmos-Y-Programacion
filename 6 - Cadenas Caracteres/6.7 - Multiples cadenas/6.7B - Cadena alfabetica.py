
def cadenaAltabetica(string1, string2):
    for l1 in string1:
        for l2 in string2:
            if l1 < l2:
                return string1
            elif l1 > l2:
                return string2
