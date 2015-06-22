def getNumChocolates(money_available, cost, wrappers):
    chocolates_bought = int(money_available / cost)
    choco_list = chocolates_bought * [None]
    i = 0
    while i <= len(choco_list):
        if i> 0 and i % wrappers == 0:
            choco_list.append(None)
        i += 1
    return len(choco_list)

num_cases = int(input())
for i in range(0, num_cases):
    money_available, cost, wrappers = input().split()
    money_available, cost, wrappers = int(money_available), int(cost), int(wrappers)
    print(getNumChocolates(money_available, cost, wrappers))