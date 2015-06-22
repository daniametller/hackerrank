# https://www.hackerrank.com/challenges/handshake

import sys
sys.setrecursionlimit(1000000)

def get_handshakes(num_members):
    # print('num mems ' +  str(num_members))
    if num_members == 0 or num_members == 1:
        return 0
    num_shakes = num_members -1
    return num_shakes + get_handshakes(num_members-1)

num_tests = int(input())
for i in range(0, num_tests):
    num_members = int(input())
    print(get_handshakes(num_members))