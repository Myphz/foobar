def solution(n):
	return len(fibonacci(n)) - len(power2(n))


def power2(n):
	l = []
	x = 0
	while sum(l) <= n:
		l.append(2 ** x)
		x += 1
	return l


def fibonacci(n):
    if n == 0: return [42]		# If n is 0, it has to return a list of 1 element.
    l = [1, 1]
    i = 1
    while sum(l) <= n:
        l.append(l[i] + l[i - 1])
        i += 1
    return l
