def solution(l):
    tested = set()
    result = {}
    count = 0
    length = len(l)
    while length > 2:
	divisors = findDivisors(l, l[-1], length - 1)
	for divisor in divisors:
	# If the divisor has already been tested before (i.e, if it is in the "tested" set), it simply picks the value from the dictionary containing the result.
	    if (divisor[0], divisor[1]) in tested: 			
	        count += result[(divisor[0], divisor[1])]
	# Else, it calculates the result and put it in the "tested" set
	    else:
	        tested.add(tuple((divisor[0], divisor[1])))
		result[(divisor[0], divisor[1])] = len(findDivisors(l, divisor[0], divisor[1]))
		count += result[(divisor[0], divisor[1])]
		
	    l.pop(length - 1)
	    length -= 1
    return count

# This function returns a list containing all the divisors of a number (e) in a list (l) up to an index (j)
def findDivisors(l, e, j):    
    divisors = []
        for i in range(j):
	    if e % l[i] == 0:
	        divisors.append((l[i], i))
return divisors
