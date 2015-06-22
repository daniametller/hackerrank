# https://www.hackerrank.com/challenges/find-maximum-index-product

# Hint: http://saraguru.weebly.com/how-i-solved/find-maximum-index-product-hackerrank

# You are given a list of N numbers a1,a2,…,an. For each i (1≤i≤N), define LEFT(i) to be the nearest index j before i such that aj>ai.
# Note that if j does not exist, we should consider LEFT(i) to be 0. Similarly, define RIGHT(i) to be the nearest index k after i such that ak>ai.
# Note that if k does not exist, we should consider RIGHT(i) to be 0.
#
# Define INDEXPRODUCT(i) as the product of LEFT(i) and RIGHT(i). Find the maximum INDEXPRODUCT(i) among all 1≤i≤N.
#
# Input Format
#
# The first line contains an integer N, the number of integers. The next line contains the N integers.
#
# Constraints:
#
# 1≤N≤10^5
# Each of the N integers will range from 0 to 109
# Output Format
#
# Output the maximum INDEXPRODUCT among all indices from 1 to N.
#
# Sample Input
#
# 5
# 5 4 3 4 5

# Sample Output
#
# 8

# Explanation
#
# We can compute the following:
#
# INDEXPRODUCT(1)=0
# INDEXPRODUCT(2)=1×5=5
# INDEXPRODUCT(3)=2×4=8
# INDEXPRODUCT(4)=1×5=5
# INDEXPRODUCT(5)=0
# The largest of these is 8, so it is the answer.

def lefts(L):
    left = [] # per cada valor L[i] quin left té
    maxes = [] # llista d'indexos
    for i in range(len(L)):
        # comparem el valor de L[i] amb L[i-1]
        while maxes and L[maxes[-1]] <= L[i]:
            maxes.pop()
        if not maxes: 
            left.append(-1)
        else: 
            left.append(maxes[-1])
        maxes.append(i) #maxes = [i]
    return left

def rights(L):
    right = []
    maxes = []
    for i in range(len(L)-1, -1, -1):
        while maxes and L[maxes[-1]] <= L[i]:
            maxes.pop()
        if not maxes: right.append(-1)
        else: right.append(maxes[-1])
        maxes.append(i) #maxes = [i]
    right.reverse()
    return right

def indexProduct(L):
    left = lefts(L)
    right = rights(L)
    products = ((left[i] + 1) * (right[i] + 1) for i in range(len(L)))
    return max(products)


if __name__ == "__main__":
    input()
    L = [int(n) for n in input().split()]
    print(indexProduct(L))