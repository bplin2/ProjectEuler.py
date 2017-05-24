from eulerlib import is_palindrome

ans = 0
for i in range(100,1000):
	for j in range(100,1000):
		x = i*j
		if is_palindrome(x) and x>ans:
			ans = i*j

print ans

#906609
