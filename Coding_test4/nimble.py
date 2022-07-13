coins = [0, 0, 0, 0]
first = 0
second = 0

for i in range(1, len(coins)):
	# print(coins[i]) gives 2,3,0,6 (since we dont have to anything with index 0)
	if coins[i]!=0:
		if coins[i]%2 == 0:
			first +=1
		else:
			if i%2 == 0:
				first +=1
			else:
				second +=1

if first>second:
	print("First")
else:
	print("Second")


# score: 8/20
# dont know whats wrong