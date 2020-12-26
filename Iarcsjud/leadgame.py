'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
l1 = []
l2 = []
s1 = []
s2 = []
k = 0
p = 0
for _ in range (int(input())):
    n1, n2 = map(int, input().split())
    n1 = n1 + k
    k = n1
    n2 = n2 + p
    p = n2
    if(n1 > n2):
        l1.append(1)
        s1.append(n1 - n2)
    else:
        l2.append(1)
        s2.append(n2 - n1)
        
if(len(s1) == 0):
    print(2, max(s2))
elif(len(s2) == 0):
    print(1, max(s1))
else:
    if(max(s1) > max(s2)):
        print(1, max(s1))
    else:
        print(2, max(s2))