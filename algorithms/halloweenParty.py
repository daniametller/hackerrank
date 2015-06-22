def getMaxPiecesWithKCuts(num_cuts):
    if num_cuts % 2 == 0:
        return int(pow(num_cuts/2, 2))
    else:
        return int(num_cuts/2) * (int(num_cuts/2) +1)


num_test_cases = int(input())
for i in range(0, num_test_cases):
    k = int(input())
    print(getMaxPiecesWithKCuts(k))