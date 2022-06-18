# s = "()[]{}"
# for brac in s:
# 	print(brac)
# print(len(s))
# print(s[2])

# Uses the concept of stack
# Link: https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
