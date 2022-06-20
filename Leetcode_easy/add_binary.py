# link: https://leetcode.com/problems/add-binary/solution/

a = '1111'
b = '0010'

x, y = int(a, 2), int(b, 2)
while y:
    answer = x ^ y
    carry = (x & y) << 1
    x, y = answer, carry
ans = bin(x)[2:]
print(ans)