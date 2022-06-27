# link: https://leetcode.com/problems/symmetric-tree/
import math


root = [1,2,2,3,4,4,3]
# print(root)
# print(len(root))
# print(root[6])

subarr = []
# for i in range(len(root)):

h = len(root)
for i in range (1, int(math.log(h+1, 2))):
    subarr = root[pow(2,i)-1 : pow(2,i+1)-1]
    # print(subarr)
    m = len(subarr)
    for j in range(int(m/2) ):
    	if(subarr[j] != subarr[m-j-1]):
    		print(1)
print(0)




# subarr1 = root[0]  
# subarr2 = root[1:3] # 2^1-1 to 2^2-1
# subarr3 = root[3:7] # 2^2-1 to 2^3-1

# print(math.log(8,2))

# # print(subarr1)
# print(subarr2)
# print(subarr3)

