sumsquare = sum(n ** 2 for n in range(1,101))
squaresum = ((100*(100+1))/2) ** 2

ans = squaresum - sumsquare

print ans
