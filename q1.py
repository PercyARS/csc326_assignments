__author__ = 'zhaopeix'

def _gcd (a,b):
    gcd = 1
    if a <= b:
        smaller = a
    else:
        smaller = b
    for i in range(1,smaller+1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
    return gcd