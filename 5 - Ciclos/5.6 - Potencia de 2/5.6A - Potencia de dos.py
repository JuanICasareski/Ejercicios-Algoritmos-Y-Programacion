
def esPotenciaDos(n):
    while 1:
        if not n%2:
            n /= 2
        else:
            return False
        if n==2 or n==1:
            return True
