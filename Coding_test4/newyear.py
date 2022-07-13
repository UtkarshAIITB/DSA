# general observation : each person would have to bribe number of people smaller than itself to reach there
# count = 0
# q = [4, 1, 2, 3]

# for i in range(len(q)):
# 	for j in range(i+1, len(q)):
# 		if q[i]>q[j]:
# 			count+=1
# 	if count>2:
# 		print(False)
# 	count = 0

# print(True)

def minimumBribes(q):
    # Write your code here
    chaotic = ''
    num_swaps = 0
    for i in range(len(q)):
        if(q[i]>i+3):
            chaotic += 'Too chaotic'
        for j in range(max(0, q[i]-2), i):
            if(q[i]<q[j]):
                num_swaps+=1

    if('Too chaotic' in chaotic):
        print('Too chaotic')
    else:
        print(num_swaps)