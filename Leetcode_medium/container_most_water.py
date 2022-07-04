# link: https://leetcode.com/problems/container-with-most-water/submissions/

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# maxi = 0
# water = 0

# for i in range(len(height)):
# 	# print(height[i])
# 	water = min(height[i], height[i+1])*1
# 	maxi = maxi+water
# 	maxi = max()

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea