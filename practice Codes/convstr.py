'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A =  list( input())
    B = list(input())
    db = dict()
    da = dict()
    cfg = 0
    ans = []
    for i in range(97, 97 + 26):
        da[chr(i)] = set()
        db[chr(i)] = set()
    for i in range(N):
        da[A[i]].add(i)
        db[B[i]].add(i)
        if (A[i] < B[i]) :
            print(-1)
            cfg = 1
            break
    count = 0
    cfr = 0
    if (cfg == 0) :
        for i in range(97 + 25, 96, -1):
            ch = chr(i)
            if (db[ch]) :
                if da[ch] :
                    c = 0
                    ind = db[ch].union(da[ch])
                    for j in ind:
                        if (A[j] != ch) :
                            c += 1
                            val = A[j]
                            da[val].discard(j)
                            A[j] = ch
                    if (c > 0) :
                        count += 1
                        ans.append(list(ind))
                else:
                    print(-1)
                    cfr = 1
                    break
        if (cfr == 0) :
            print(count)
            for x in ans :
                le = len(x)
                print(le, end=" ")
                for i in range(le):
                    print(x[i], end=" ")
                print()


