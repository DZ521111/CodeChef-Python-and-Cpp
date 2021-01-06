'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
R, C  = map(int, input().split())

for _ in range(C - 1):
    print("R", end = "")
print("U", end = "")
for _ in range(C - 1):
    print("L", end = "")
print()
