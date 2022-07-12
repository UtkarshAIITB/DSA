# link : https://leetcode.com/problems/excel-sheet-column-title/

alpha_map = {i+1 :chr(i+65) for i in range(26)}
columnNumber = 701

res = ''
# res += 'A'
# print(res)


while(columnNumber>26):
	rem = columnNumber%26
	columnNumber = columnNumber//26
	res+=alpha_map[rem]

res+= alpha_map[columnNumber]
print(res[::-1])


# while num > 0:
#     result.append(capitals[(num-1)%26])
#     num = (num-1) // 26
# print(alpha_map)