# https://www.hackerrank.com/challenges/truck-tour
def where_can_i_start(pump_list):
    min_balance = 9999999
    i = 0
    position = 0
    balance = 0
    while i < len(pump_list):
        balance += pump_list[i][0]- pump_list[i][1]
        if balance < min_balance:
            min_balance = balance
            position = (i + 1) % len(pump_list)
        i += 1
    return position

pump_list = []
num_pumps = int(input())
for i in range(0, num_pumps):
    pump_list.append([int(numeric_string) for numeric_string in input().split()])

print(where_can_i_start(pump_list))