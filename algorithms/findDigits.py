def getDividers(num):
    num_list = [int(x) for x in str(num)]
    count = 0
    for i in range(0, len(num_list)):
        if num_list[i] != 0 and num % num_list[i] == 0:
            count += 1
    return count

num_cases = int(input())
for i in range(0, num_cases):
    num = int(input())
    print(getDividers(num))