def solution(N):

    if N < 2:
        return [1,2]
    resoul=[]
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            resoul.append([i,int(N/i)])
    finiszer=[]
    for l in resoul:
        finiszer.append(2*(l[0]+l[1]))
    return min(finiszer)
print(solution(30))
