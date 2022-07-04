def poisonousPlants(p, count):
	# return(p)
	# count = 0
	lst = p.copy()
	
	for i in range(1,len(p)):
		if p[i-1]<p[i]:
			# count+=1
			lst.remove(p[i])
	if lst == p:
		return count
	else:
		count += 1
		return poisonousPlants(lst, count)


p = [6, 5, 8, 4, 7, 10, 9]
count = 0
# print(poisonousPlants(p))
ret = poisonousPlants(p, count)
print(ret)

# this solutions fails to pass certain test cases since lst.remove won't work if p
# contains two pesticides with same value. Then remove function directly removes the
# first such element.

# Hence gives a score of 40/70