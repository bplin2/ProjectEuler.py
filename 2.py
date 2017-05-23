ans = 0
a = 1
b = 2

while a  <= 4000000:
	if a%2 == 0:
		ans += a
	temp = a
	a = b
	b = b + temp

print ans

#4613732
