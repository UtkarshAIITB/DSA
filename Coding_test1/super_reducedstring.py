# s = 'aa'
# copy = s
# print(len(s))
# print(copy)

# # for i in range (len(s)):
# # 	if s[i] == s[i+1]:
# copy = list(s)
# print(copy)
# m = len(copy)
# for i in range (m-1):
# 	if copy[i] == copy[i+1]:
# 		copy[i] = ''
# 		copy[i+1] = ''

# print(copy)
# final = ''.join(copy)
# print(final)
# # print(len(final))
# just = ''
# print(just)


def superReducedString(s):
    final2 = s
    if final2 == '':
        return 'Empty String'
    copy = list(s)
    for i in range(len(copy)-1):
        if copy[i] == copy[i+1]:   
            copy[i] = ''
            copy[i+1] = ''
    final = ''.join(copy)
    if final == final2:
        return (final2)
    else:
        return superReducedString(final)

