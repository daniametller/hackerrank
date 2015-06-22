# https://www.hackerrank.com/challenges/find-maximum-index-product

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

def get_max_index_product(list, index):
    if list == None:
        return
    i, j = index, index
    left = 0
    right = 0
    while i >= 0:
        if list[i] > list[index]:
            left = i + 1
            break
        i -= 1

    while j < len(list):
        if list[j] > list[index]:
            right = j + 1
            break
        j += 1
    return left * right

list = []
max_index = 0
list_length = int(input())
list = [int(j) for j in input().split()]
for j in range(0, len(list)):
    index = get_max_index_product(list, j)
    if index > max_index:
        max_index = index
print(max_index)
