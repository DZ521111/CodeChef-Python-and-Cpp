'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
m = input()
lst = list(map(int, input().split()))
case = int(input())
for _ in range(case):
	i = int(input())
	print(lst.pop(i-1))