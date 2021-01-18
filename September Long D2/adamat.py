'''
Author : Dhruv B Kakadiya

'''
# cook your dish here
for _ in range(int(input())):
    order = int(input())
    mat, ans, count = [], 0, 0
    for __ in range(order):
        mat.append(list(map(int, input().split())))
    j = order
    while (True):
        if (mat[0][j - 1] != j):
            mat = [[mat[y][x] for y in range(j)] for x in range(j)]
            ans += 1
            #print(mat)
        else:
            j -= 1
            count += 1
        if (count == order):
            break
    print(ans)