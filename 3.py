from math import sqrt
from eulerlib import primes

def prime_factor(x):
	prime = primes(sqrt(x))
	for num in prime:
		if x%num == 0:
			print num

prime_factor(600851475143)

#6857
