# link : https://leetcode.com/problems/excel-sheet-column-number/
columnTitle = 'AB'

# s = list(columnTitle)
# print(s)

#  AB = 28
#  A*26^1 + B*26^0 = 26+2 = 28
# create a mapping first

# print(chr(65))               prints A

alpha_map = {chr(i+65): i+1 for i in range(26)}
n = len(columnTitle)

sumty = 0
lst = list(columnTitle)

for i in range(n):
	sumty = sumty + alpha_map[lst[i]]*pow(26,n-i-1)

print(alpha_map)
print(sumty)
# print(alpha_map['A'])