__author__ = 'zhaopeix'
import doctest
import unittest


_list = []
def isPrime(N):
    """Return if N is a prime number of not

    >>> isPrime(1)
    True
    >>> isPrime(2)
    True
    >>> isPrime(19)
    True
    >>> isPrime(100)
    False
    >>> isPrime(42342)
    False
    """
    ret = -1
    if N == 1:
        return True
    for i in range(1,N):
        if (N % i == 0):
            ret = i
    if ret == 1:
        return True
    else:
        return False

def factorize_helper(N,_list):
    if N == 1:
        _list.append(1)
    else:
        greatest_prime_factor = -1
        for i in range(1,N+1):
            if (N % i == 0):
                if isPrime(i) == True:
                    greatest_prime_factor = i
        factorize_helper(N / greatest_prime_factor,_list)
        if greatest_prime_factor not in _list:
            _list.append(greatest_prime_factor)


def factorize(N):
    """Return all the prime factors in an ordered list
    >>> factorize(1)
    [1]
    >>> factorize(10)
    [1, 2, 5]
    >>> factorize(19)
    [1, 19]
    >>> factorize(100)
    [1, 2, 5]
    >>> factorize(42342)
    [1, 2, 3, 7057]
    """
    ret = []
    factorize_helper(N,ret)
    return ret

doctest.testmod()