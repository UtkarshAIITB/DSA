s = '{[()]}'
stack = []
maps = {')':'(', '}':'{', ']':'['}

for char in s:
	if char in maps:
		top_element = stack.pop() if stack else '#'

		if maps[char] != top_element:
			print( False)

	else:
		stack.append(char)
print( True)