listlengh=int(input())
array=list(map(int,input().split()))
setarray=set(array)
resultdict={}
for index in range(min(array),max(array)+1):
    resultdict[index]=0
finalstring=""
for num in array:
    resultdict[num]+=1
for element in resultdict:
    if resultdict[element]!=0:
        for _ in range(resultdict[element]):
            finalstring+=str(element)+" "
print(finalstring)
