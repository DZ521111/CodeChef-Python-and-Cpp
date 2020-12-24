'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
primes = {3, 5, 7, 11, 13, 17}  # sums are between 3 and 18
# and all possible exchanges
adiacent_coords = set(
    (3*x1 + x2, 3*y1 + y2)
    for x1 in range(3) for x2 in range(3)  # all cells
    for y1, y2 in ((x1 + 1, x2), (x1, x2 + 1)) # al down and right adiacent
    if y1 < 3 and y2 < 3 # y should be inside
)

solvable = {}
checking = [(0, (1,2,3,4,5,6,7,8,9))] # solved state
while checking:
    moves, state = checking.pop(0) # take first state
    moves += 1 # the state obtained from this will need another move
    for x,y in adiacent_coords:
        if state[x] + state[y] in primes:  # the moves is valid
            nstate = list(state)  # unfreezing
            nstate[x], nstate[y] = nstate[y], nstate[x]  # doing the swap
            nstate = tuple(nstate)  # freezing so it's hashable
            if nstate not in solvable:  # it's new?
                checking.append((moves, nstate))
                solvable[nstate] = moves
# now we have the whole set of solvables
for _ in range(int(input())):
    input() # skipping blankline
    puzzle = tuple(sum((
        [int(i) for i in input().strip().split(" ")] # read a line
        for _ in range(3)
    ), []))
    try:
        print(solvable[puzzle])
    except KeyError:  # it's not solvable
        print(-1)
        