cost = [1, 3, 4, 5, 6]
m = 6

# output 1,4 as indexes

for i in range(len(cost)):
	for j in range(i, len(cost)):
		if cost[j] == m - cost[i] and i!=j:
			print(i+1, j+1)