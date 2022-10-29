q=list(map(int,input().split()))
qset=set(q)

resultdict={}
for element in qset:
    resultdict[element]=0

for num in q:
    resultdict[num]+=1

indexmax=max(resultdict.values())
comparelist=[]
for numbers in resultdict:
    if resultdict[numbers]==indexmax:
        comparelist.append(numbers)

print(max(comparelist))