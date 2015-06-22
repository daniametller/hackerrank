# https://www.hackerrank.com/challenges/pangrams
def is_pangram(input):
    data = input.lower().replace(' ', '')
    data = "".join(set(data))
    if len(data) == 26:
        return "pangram"
    else:
        return "not pangram"


data = input()
print(is_pangram(data))