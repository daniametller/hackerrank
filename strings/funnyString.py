# https://www.hackerrank.com/challenges/funny-string
#
# Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S.
# The string S is funny if the condition |Si−S(i−1)|=|Ri−R(i−1)| is true for every i from 1 to N−1.
#
# (Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str.
# |x| denotes the absolute value of an integer x)
#
# Input Format
#
# First line of the input will contain an integer T. T testcases follow. Each of the next T lines contains one string S.
#
# Constraints
#
# 1<=T<=10
# 2<=length of S<=10000
# Output Format
#
# For each string, print Funny or Not Funny in separate lines.

# Sample Input
#
# 2
# acxz
# bcxz
#
# Sample Output
#
# Funny
# Not Funny

def is_funny(item):
    reversed = item[::-1]
    i = 0
    while i < len(item) -1:
        if abs(ord(item[i+1]) - ord(item[i])) != abs(ord(reversed[i+1]) - ord(reversed[i])):
            return "Not Funny"
        i += 1
    return "Funny"

num_test_cases = int(input())
for i in range(0, num_test_cases):
    item = input()
    print(is_funny(item))