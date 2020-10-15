def solution(x,y):
    s = 0
    x, y = int(x), int(y)
    if x == y: return "impossible"
    while (x,y) != (1,1) and x > 0 and y > 0:
        if x > y: 
	    a = x//y
	    if a == x: a -= 1
	        x -= y * a
		s += a
	else:
	    a = y//x
	    if a == y: a -= 1		 
	    y -= x * a
	    s += a
    return str(s) if (x,y) == (1,1) else "impossible"
