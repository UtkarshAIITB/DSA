# link : https://leetcode.com/problems/unique-paths/

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m==1 or n==1:
#             return 1
#         return (self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1))

# the above solution has problems with time limit.


# dynamic programming, a faster approach

m = 3
n = 7
d = [[1] * n for _ in range(m)]
# print(d)

for row in range(1,m):
	for col in range(1,n):
		d[row][col] = d[row-1][col] + d[row][col-1]

return d[m-1][n-1]