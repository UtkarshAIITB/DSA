steps = 8
path = 'UDDDUDUU'


alt = 0
valley = 0
lis = [0]

for step in path:
# print(step)
	if step == 'U':
		alt += 1
	if step == 'D':
		alt -= 1
	lis.append(alt)

print(lis)

for i in range(len(lis)-1):
	if lis[i]==0 and lis[i+1]<0:
		valley+=1

print(valley)

