tasks = [2,2,3,3,2,4,4,4,4,4]
hashmap = {}

for task in tasks:
	if task not in hashmap:
		hashmap[task] = 1
	else:
		hashmap[task] +=1

# print(hashmap)
count = 0

for key in hashmap:
	# print(hashmap[key])
	if hashmap[key] == 1:
		print(-1)
	else:
		count += (hashmap[key]+2)//3

print(count)