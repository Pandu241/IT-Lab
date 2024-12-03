def check_two_equal(x, y, z):
    if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        return 1
    return 0
	
def integer_division(a, b):
    if b == 0:
        return -1, -1  # If b is 0
    q, r = 0, a
    while r >= b:
        r -= b
        q += 1
    return q, r
	
def largest_square(n):
    k = 0
    q = 0
    while (k + 1) ** 2 <= n:
        k += 1
        q = k ** 2
    return q