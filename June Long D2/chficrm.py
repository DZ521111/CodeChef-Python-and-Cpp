'''
Author : Dhruv B Kakadiya
'''

result = []
for _ in range(int(input())):
    n = int(input())
    chef = []
    coin = list(map(int, input().split()))
    if (coin[0] == 5):
        chef.append(5)
        for i in range(1, n):
            if (coin[i] == 5):
                chef.append(coin[i])
            elif ((coin[i] == 10) and (5 in chef)):
                chef.remove(5)
                chef.append(coin[i])
            elif ((coin[i] == 15) and ((10 in chef) or (chef.count(5) >= 2))):
                if (10 in chef):
                    chef.remove(10)
                else:
                    chef.remove(5)
                    chef.remove(5)
                chef.append(coin[i])
            else:
                result.append("NO")
                break
        else:
            result.append("YES")
    else:
        result.append("NO")
for j in result:
    print(j)
    
