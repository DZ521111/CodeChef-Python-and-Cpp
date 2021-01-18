import math as m
def find_index(sum_):
    index_ = (m.sqrt((sum_ * 4) + 1) - 1) // 2
    return int(index_)

for _ in range(int(input())):
    n = int(input())
    total = ((n * (n + 1)) // 2)
    if (total % 2 == 0):
        i = find_index(total)
        if ((total // 2) == ((i * (i + 1)) // 2)):
            print(((i * (i - 1)) // 2) + (((n - i) * ((n - i) - 1)) // 2) + (n - i))
        else:
            print(n - (i + 1) + 1)
    else:
        print(0)