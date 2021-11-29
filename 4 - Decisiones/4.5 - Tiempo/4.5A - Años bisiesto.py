
def esBisiesto(año):
    if not año%4 and (año%100 or not año%400):
        return True
    return False
    