arr = [7,2,5,3,5,3]
brr = [7,2,5,4,6,3,5,3]

# print(arr)
hashmap = {}
for nums in arr:
	# print(nums)
	if nums not in hashmap:
		hashmap[nums] = 1
	else:
		hashmap[nums]+=1

print(hashmap)

hashmap2 = {}

for nums in brr:
	if nums not in hashmap2:
		hashmap2[nums] = 1
	else:
		hashmap2[nums] += 1

print(hashmap2)

list2 = []

# print(hashmap2[5])
for key in hashmap2:
	if key not in hashmap:
		list2.append(key)
	if key in hashmap and hashmap[key]!=hashmap2[key]:
		list2.append(key)

print(list2) 
list2.sort()
print(list2)
