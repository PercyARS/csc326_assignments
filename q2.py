__author__ = 'zhaopeix'

def rotate_word(_string, i):
    ret = ""
    a = i % len(_string)
    for n in range(len(_string)):
        char = _string[n + a - len(_string)]
        ret += char
    return ret

print rotate_word("abc",1)

