# https://leetcode.com/problems/pascals-triangle/submissions/
# dynamic programming


triangle = []
# row = [1]
# triangle.append(row)
# row2 = [1,1]
# triangle.append(row2)
# print(triangle)

num_rows = 5
for i in range(num_rows):
	row = [0]*(i+1)
	row[0] , row[len(row)-1] = 1,1
	triangle.append(row)

for i in range(2,num_rows):
	row1 = triangle[i-1]
	row2 = triangle[i]
	j = 1
	for m in range(1, len(row2)-1):
		row2[m] = row1[j]+row1[j-1]
		j+=1
	triangle[i] = row2


# i = 2
# row = [0]*(i+1)
# print(row)
print(triangle)
print(triangle[3])
print(triangle[3][2])
