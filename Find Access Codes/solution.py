def solution(l):
	tested = set()	# making it a set so it's way faster searching elements in it
	result = {}
	count = 0
	length = len(l)
	while length > 2:
		divisors = findDivisors(l, l[-1], length - 1)
		for divisor in divisors:
			if (divisor[0], divisor[1]) in tested: 			# if the divisor has already been tested before, it just picks the value from the dictionary.
				count += result[(divisor[0], divisor[1])]
			else:											# else, it calculates it and adds it to the dictionary
				tested.add(tuple((divisor[0], divisor[1])))
				result[(divisor[0], divisor[1])] = len(findDivisors(l, divisor[0], divisor[1]))
				count += result[(divisor[0], divisor[1])]
		l.pop(length - 1)
		length -= 1
	return count


def findDivisors(l, e, j):    # finds all of the divisors of e in the list l up to index j
	divisors = []
	for i in range(j):
		if e % l[i] == 0:
			divisors.append((l[i], i))
	return divisors