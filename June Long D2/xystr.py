'''
Author : Dhruv B Kakadiya
'''

result = []
for _ in range(int(input())):
    s = input()
    count = 0
    i = 0
    while(i+1 < len(s)):
        if (s[i] != s[i+1]):
            count += 1
            i += 2
        else:
            i += 1
    result.append(count)
for j in result:
    print(j)
