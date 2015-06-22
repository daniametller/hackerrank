# https://www.hackerrank.com/challenges/journey-to-the-moon

# The member states of the UN are planning to send 2 people to the Moon. But there is a problem.
# In line with their principles of global unity, they want to pair astronauts of 2 different countries.
#
# There are N trained astronauts numbered from 0 to N-1.
# But those in charge of the mission did not receive information about the citizenship of each astronaut.
# The only information they have is that some particular pairs of astronauts belong to the same country.
#
# Your task is to compute in how many ways they can pick a pair of astronauts belonging to different countries.
# Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know their country directly.
# For instance, if 1,2,3 are astronauts from the same country;
# it is sufficient to mention that (1,2) and (2,3) are pairs of astronauts from the same country without providing information about a third pair (1,3).
#
# Input Format
# The first line contains two integers, N and I, separated by a single space. I lines follow.
# Each line contains 2 integers separated by a single space A and B such that
#
# 0 ≤ A, B ≤ N-1
#
# and A and B are astronauts from the same country.
#
# Output Format
# An integer that denotes the number of permissible ways to choose a pair of astronauts.
#
# Constraints

# 1<=N<=105
# 1<=I<=104
#
# Sample Input
#
# 4 2
# 0 1
# 2 3

# Sample Output
#
# 4

# Explanation

# Persons numbered 0 and 1 belong to same country, and those numbered 2 and 3 belong to same country. So the UN can choose one person out of 0 & 1 and another person out of 2 & 3. So number of ways of choosing a pair of astronauts is 4.


N, I = map(int, input().strip().split())
assert 1 <= N <= 10**5
assert 1 <= I <= 10**6
lis_of_sets = []

for i in range(I):
    a,b = map(int, input().strip().split())
    assert 0 <= a < N and 0 <= b < N
    indices = []
    new_set = set()
    set_len = len(lis_of_sets)
    s = 0
    while s < set_len:
        if a in lis_of_sets[s] or b in lis_of_sets[s]:
            indices.append(s)
            new_set = new_set.union(lis_of_sets[s])
            del lis_of_sets[s]
            set_len -= 1
        else:
            s += 1

    new_set = new_set.union([a, b])

    lis_of_sets.append(new_set)

answer = N*(N-1)/2
for i in lis_of_sets:
    answer -= len(i)*(len(i)-1)/2

print(int(answer))