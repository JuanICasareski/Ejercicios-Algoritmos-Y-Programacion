
def algoritmoEuclides(n, m):
    while 1:
        r = m % n
        if r == 0:
            return n
        m, n = n, r
