#Level 3 Exercise 3: Find all lucky tuples (x,y,z) in a list where x divides y and y divides z.
def solution(l):
	tested = set()
	result = {}
	count = 0
	length = len(l)
	while length > 2:
		divisors = findDivisors(l, l[-1], length - 1)
		for divisor in divisors:
			if (divisor[0], divisor[1]) in tested:
				count += result[(divisor[0], divisor[1])]
			else:
				tested.add(tuple((divisor[0], divisor[1])))
				result[(divisor[0], divisor[1])] = len(findDivisors(l, divisor[0], divisor[1]))
				count += result[(divisor[0], divisor[1])]
		l.pop(length - 1)
		length -= 1
	return count


def findDivisors(l, e, j):
	divisors = []
	for i in range(j):
		if e % l[i] == 0:
			divisors.append((l[i], i))
	return divisors