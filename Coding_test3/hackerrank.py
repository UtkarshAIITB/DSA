s = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
right = 'hackerrank'
left = 'knarrekcah'
# count = 0
lst1 = list(left)
lst2 = list(s)


for char in s:
	if len(lst1) != 0:
		if char == lst1[-1]:
			lst1.pop()
	else:
		break

if len(lst1) == 0:
	print('YES')
else:
	print('NO')

# print(lst1)
# lst1.pop()
# print(lst1)


# print(lst1)
# print(lst1[-1])
# lst1.pop()
# print(lst1)





