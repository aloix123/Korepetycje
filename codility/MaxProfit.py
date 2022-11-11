def solution(A):

    smaleststock=A.index(min(A))
    leftA=A[smaleststock:]
    leftresult=0
    for num in leftA:
        pass
    rightA=A[:smaleststock]
    print(smaleststock)
print(solution([23171,
   21011,
   21123,
   21366,
   21013,
   21367]))