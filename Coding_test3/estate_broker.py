# m unsold houses
# each house has an area xj and min price yj

# n clients
# wants house with area>ai and price less than pi

clients = [[5,110], [9,500], [20,400]]
houses = [[10,100], [2,200], [30,300]]
count = 0

# print(houses[0])
# aim : to return maximum number of houses that we can sell
# print(houses)
houses.sort(key=lambda l:l[1])
print(houses)

clients.sort(key = lambda l:l[1])
print(clients)

# for house in houses:
# 	for client in clients:
# 		if client[1]>house[1] and client[0]<house[0]:
# 			count +=1
# 			clients.remove(client)
# 			houses.remove(house)
# print(count)
# houses.remove([10,100])
# print(houses)

# for house in houses:
	# print(house[0])


# print(houses)