from math import sqrt
from eulerlib import primes

def prime_factor(x):
	ans = 0
	prime = primes(sqrt(x))
	for num in reversed(prime):
		if x%num == 0 and num > ans:
			ans = num
			print ans

prime_factor(600851475143)

#6857
