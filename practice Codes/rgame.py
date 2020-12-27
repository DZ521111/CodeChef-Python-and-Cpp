'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
if __name__ == '__main__':
	for _ in range(int(input())):
		n = int(input())
		m1 = list(map(int,input().split()))
		m=10**9+7
		n=len(m1)
		total=0
		l=2*(m1[0])
		p=1
		for i in range(1,n):
		    total =(2*total + l*m1[i])%m
		    p=(p*2)%m
		    l=(l+m1[i]*p)%m
		print(total)
