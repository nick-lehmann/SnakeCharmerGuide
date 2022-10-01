def max(l):
    max = 0
    for element in l:
        if element > max:
            max = element
    return max


def sum(l):
    s = 0
    for element in l:
        s += element
    return s


def sqrt(x):
    return x ** (1/2)
