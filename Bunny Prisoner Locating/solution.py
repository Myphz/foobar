# Definitely not the best solution, as it calculates all of the combinations up to the last one, and just returns the last one.
# Anyway, it works and it's fast enough because the numbers are pretty small
def getStart(n):
    s = 1
    for i in range(0,n):
        s += i
    return s


def solution(x, y):
    l = [getStart(y)]
    for i in range(2,x + 1):
        l.append(l[i-2] + i + y-1)
    return str(l[-1])