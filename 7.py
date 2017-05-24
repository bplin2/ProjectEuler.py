from eulerlib import is_prime

x = 1
n = 0
while n != 10001:
	x += 1
	if is_prime(x):
		n += 1

print x
