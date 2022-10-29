
def solution(N):

    divided_numbers = []

    testetnumber = N
    if N <2:
        return 0
    i = 2
    while i <= int(testetnumber ** 0.5) + 1:
        if N % i == 0:
            divided_numbers.append(i)
        i += 1
    return len(divided_numbers)+1
print(solution(24))