# Definitely not the best solution, as it calculates all of the sequence numbers up to the last one, and just returns the last one.
# Anyway, it works and it's fast enough because the numbers are pretty small

# This function is useful to determine the starting point of the sequence, given the height (n).
def getStart(n):
    s = 1
    for i in range(0,n):
        s += i
    return s

# It calculates every single value of the sequence and returns the last one.
def solution(x, y):
    l = [getStart(y)]
    for i in range(2,x + 1):
        l.append(l[i-2] + i + y-1)
    return str(l[-1])
