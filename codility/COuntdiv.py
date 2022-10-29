def solution(A,B,K):
    T=[x for x in range(A,B)]

    result=0
    for num in T:
        if num%K==0:
            result+=1
    print(result)
    return result
solution(6,11,2)