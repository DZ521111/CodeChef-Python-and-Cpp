'''
Author : Dhruv B Kakadiya
'''

# cook your dish here
result = []
for _ in range(int(input())):
    N, K = map(int, input().split())
    sum_ = 0
    price = list(map(int, input().split()))
    if(K in price):
        price = list(filter(lambda a:a != K, price))
    price.sort()
    for x in enumerate(price):
         if x[1] > K:
             index_ = x[0]
             break
    else:
        index_ = -1
    if (index_ != -1):
        for i in range(index_, len(price)):
            sum_ += (price[i] - K)
    result.append(sum_)
for j in result:
    print(j)