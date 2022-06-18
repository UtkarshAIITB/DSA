strs = ["flower","flow","flight"]
shortest = min(strs, key = len) 
print(len(strs))
# print(shortest) # outputs flow
def longestcommonprefix(self, strs):
	for i, ch in enumerate(shortest):
		print(i, ch)
		# print(ch)
		# for other in strs:
		# 	print(other)
		for other in strs:
			# print(other[i])
			if other[i] != ch:
				return shortest[:i]
	return shortest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ''
        shortest = min(strs, key = len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i]!= ch:
                    return shortest[:i]
        return shortest