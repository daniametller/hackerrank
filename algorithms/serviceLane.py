highwayLength, numCases = input().split()
highwayLength, numCases = int(highwayLength), int(numCases)
widthsArray = [int(numeric_string) for numeric_string in input().split()]

def getMaxAllowedWidth(i, j):
    minWidth = 3
    for x in range(i, j+1):
        if widthsArray[x] < minWidth:
            minWidth = widthsArray[x]
    return minWidth

for i in range(0, numCases):
    i, j = input().split()
    i, j = int(i), int(j)
    print(getMaxAllowedWidth(i, j))