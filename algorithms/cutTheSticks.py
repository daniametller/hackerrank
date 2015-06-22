def popZeroes(sticks):
    i = 0
    while i< len(sticks):
        if sticks[i] == 0:
            sticks.pop(i)
            i = 0
        else:
            i += 1
    return sticks

def cut(sticks):
    sticks = popZeroes(sticks)
    if not sticks:
        return -1, []
    sticks.sort()
    shortest_stick = sticks[0]
    num_sticks_cut = 0
    for i in range (0, len(sticks)):
        sticks[i] -= shortest_stick
        num_sticks_cut += 1

    return num_sticks_cut, sticks

numSticks = int(input())
stickArray = [int(numeric_string) for numeric_string in input().split()]

while len(stickArray) > 0:
    num_cuts, stickArray = cut(stickArray)
    if num_cuts == -1:
        continue
    print(num_cuts)
