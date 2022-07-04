# link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

# digits = '23'




# alpha_map = {i+1 : [chr(3*(i-1)+97), chr(3*(i-1)+98), chr(3*(i-1)+99)] for i in range(1,9)}
# # print(alpha_map)
# alpha_map[7].append('s')
# alpha_map[8].remove('s')
# alpha_map[8].append('v')
# alpha_map[9].remove('v')
# alpha_map[9].append('y')
# alpha_map[9].append('z')

# for dig in digits:
	# print(dig)

# print(alpha_map)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha_map = {str(i+1) : [chr(3*(i-1)+97), chr(3*(i-1)+98), chr(3*(i-1)+99)] for i in range(1,9)}
        alpha_map['7'].append('s')
        alpha_map['8'].remove('s')
        alpha_map['8'].append('v')
        alpha_map['9'].remove('v')
        alpha_map['9'].append('y')
        alpha_map['9'].append('z')
        
        if len(digits) == 0:
            return []
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = alpha_map[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations            