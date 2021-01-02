'''
Author : Dhruv B Kakadiya

'''

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        john = list(map(int, input().split()))
        jack = list(map(int, input().split()))
        john_sum = sum(john)
        jack_sum = sum(jack)
        swapping = 0
        if (n <= m):
            looping = n
        else:
            looping = m
        if (john_sum > jack_sum):
            print(0)
        else:
            for i in range(looping):
                min_john, max_jack = min(john), max(jack)
                john.remove(min_john)
                john.append(max_jack)
                jack.remove(max_jack)
                jack.append(min_john)
                john_sum, jack_sum = sum(john), sum(jack)
                swapping += 1
                if (john_sum > jack_sum):
                    print(swapping)
                    break
            else:
                print(-1)