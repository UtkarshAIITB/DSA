# n = 3
# c = [8,3,1,2]

# def getWays(n,c):
# 	if n == 0:
# 		return 1
# 	if n<0:
# 		return 0
# 	if n>0:
# 		count = 0
# 		for i in range(len(c)):
# 			n = n-c[i]
# 			count = count+getWays(n,c)
# 	return count

n = 3
c = [8,3,1,2]


def getWays(n, c):
    dp = [0]*(n+1)
    dp[0] = 1
    
    for den in c:
        for x in range(den, n+1):
            dp[x] += dp[x-den]
    return dp[n]

# print(getWays(n,c))
