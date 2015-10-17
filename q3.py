__author__ = 'zhaopeix'

seen_dict = {}
def fib(n, l):
    l.append(n)
    if n in seen_dict.keys():
        return seen_dict[n]
    if n == 0 or n == 1:
        seen_dict[n] = n
        return n
    else:
        ret = fib(n-1,l) + fib(n-2,l)
        seen_dict[n] = ret
        return ret

list = []
print fib(6,list)
print list
