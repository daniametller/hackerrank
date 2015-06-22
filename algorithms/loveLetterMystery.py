def charPosition(letter):
    return ord(letter) - 97

def isPalindrome(st):
    if st == st[::-1]:
        return True
    else:
        return False

def palindromize(candidate):
    candidateList = list(candidate)
    i = 0
    numSteps = 0
    j = len(candidateList) - 1
    while i < j:
        frontCharPos = ord(candidateList[i])
        backCharPos = ord(candidateList[j])
        if frontCharPos != backCharPos:
            numSteps += abs(frontCharPos - backCharPos)
        i +=  1
        j -=  1

    return numSteps

numTestCases = int(input())
for i in range(0, numTestCases):
    candidate = input()
    # if len(candidate) < 2 or isPalindrome(candidate):
    #     print(0)
    # else:
    print(palindromize(candidate))

