carNumber=int(input())
directions=list(map(int,input().split()))
west=0
east=1
result=0
for direct in range(len(directions)):
    if directions[direct]==west:
        for otherdirect in directions[direct:]:
            if otherdirect==east:
                result+=1
print(result)