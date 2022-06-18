# x = 192
# print(x//10)
# print(x%10)
def isPalindrome(x: int) -> bool:
	if( (x<0) or (x % 10 == 0 and x != 0)):
		return False
	
	temp = 0
	copy = x
	while(x!=0):
	    temp = (x%10) + temp
	    temp = temp*10
	    x = x//10
	if (temp/10 == copy):
	    return True
	else:
	    return False

print(isPalindrome(11))
print(isPalindrome(10))
print(isPalindrome(-121))
print(isPalindrome(121))