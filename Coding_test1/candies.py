n = 3
arr = [9,8,7,6,5,4,3,2,1]
# arr = [2,4,3,5,2,6,4,5]
# arr = [1, 2, 2]
list3 = [1]*len(arr)

for i in range(len(arr)-1):
	if arr[i]<arr[i+1]:
		list3[i+1] = list3[i]+1
	# if arr[i]>arr[i+1]:
	# 	if list3[i] == 1:
	# 		list3[i]+=1
	# 	if(i!=0 and list3[i] == list3[i-1]):
	# 		list3[i-1]+=1
	# if arr[i] == arr[i+1] and list3[i]>list3[i+1]:
	# 	list3[i] = list3[i]+1
j = len(arr)-1
while(j>0):
	if arr[j-1]>arr[j]:
		list3[j-1] = max(list3[j-1], list3[j]+1)
	j = j-1
# for j in range(0, len(arr)-1):
# 	if arr[j+len(arr)-1]<arr[j+len(arr)-2]



# print(arr[len(arr)-1])
print(arr)
print(list3)
# print(sum(list3))

# for i in range(len(arr)-1):
# 	print(i)

# print(arr[8])