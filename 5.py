check = [11,13,14,16,17,18,19,20]

def lcm(x):
	ans = [n for n in check if x%n == 0]
	if ans == check:
		return x
	return 0

for x in xrange(2520, 1000000000, 2520):
	if lcm(x) != 0:
		print lcm(x)
		break

#232792560
	


