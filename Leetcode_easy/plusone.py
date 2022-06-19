digits = [1,2,3]
# print(len(digits))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = len(digits)
        
        for i in range(m):
            if digits[m-i-1] == 9:
                digits[m-i-1] = 0
            else:
                digits[m-i-1] += 1
                return digits
        
        return [1]+digits