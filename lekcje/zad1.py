A=list(map(int,input().split(",")))
def find_first_even(A):
    leftindex=0;rightindex=len(A)-1
    while leftindex<=rightindex:
        middle=(leftindex+rightindex)//2
        if A[middle]%2==0:
            rightindex=middle-1
        else:
            leftindex=middle+1
    return A[leftindex]
print(find_first_even(A))

