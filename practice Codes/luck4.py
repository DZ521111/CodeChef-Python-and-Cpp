'''
Author : Dhruv B Kakadiya

'''


result = []
for _ in range(int(input())):
    num = int(input())
    num_string = str(num)
    count_ = num_string.count('4')
    result.append(count_)
for i in result:
    print(i)