'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
def pal(str):
    h=len(str)//2
    i=0
    j=len(str)-1
    for k in range(h):
        if(str[i]!=str[j]):
            return False
        i=i+1
        j=j-1
    return True
n=int(input())
s=(input())
max=0
for i in range(1,n+1):
    for j in range(0,n):
        if(j+i > n):
            break;
        str=s[j:j+i]
        if(pal(str) and len(str)>max):
            max=len(str)
            l=str
print(max)
print(l)
