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


def average(l):
    return sum(l)/len(l)


def median(l):
    l = sorted(l)
    size = len(l)
    middle = size // 2
    median = l[middle]
    if size % 2 == 0:
        median = (median+l[middle+1]) / 2
    return median
