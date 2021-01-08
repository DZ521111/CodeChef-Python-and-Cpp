import sys
range = xrange
def input(x = 1, store = []):
    while len(store) < x:
        store += raw_input().split()
    if x == 1:
        return store.pop(0)
    else:
        return [store.pop(0) for _ in range(x)]


t = int(input())
for _ in range(t):
    n,y = int(input()), int(input())
    n = 10**6

    a = -1
    b = n//2 + 10

    aval = -1
    bval = 0

    # ind = a * 2 + 1
    
    while a + 1 < b:
        c = a + b >> 1

        ind = 2 * c + 1
        print 1, 2 * c + 1
        sys.stdout.flush()

        x = int(input())
        if x == 0:
            bval = 0
            b = c
        elif x == y:
            a = c
            aval = x
            break
        elif x > y:
            b = c
            bval = x
        else:
            a = c
            aval = x

    if a == -1:  
        print 2, -1
        sys.stdout.flush()
        s = input()
        assert(s == 'YES')
        continue

    if aval == y:
        print 2, 2 * a + 1
        sys.stdout.flush()
        s = input()
        assert(s == 'YES')
        continue

    # Answer must if exists be at ind
    ind = 2*a + 2

    pow2 = 2
    while ind % (2 * pow2) == 0:
        pow2 *= 2
    

    print 1, ind
    sys.stdout.flush()
    val = int(input())
    
    if val == 0:  
        print 2, -1
        sys.stdout.flush()
        input()
        continue
    
    while pow2 != 2:
        pow2 //= 2
        if ind + pow2 <=n:
            print 1, ind + pow2
            sys.stdout.flush()
            val -= int(input())
    
    val -= bval

    if val == y:
        print 2,ind
    else:
        print 2, -1
    sys.stdout.flush()
    s = input()
    assert(s == 'YES')

