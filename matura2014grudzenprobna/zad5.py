def readfile():
    with open("dziennik.txt","r") as dziennik:
        x=[int(x.strip()) for x in dziennik.readlines()]
    return x
diary=readfile()
def zad53(data):
    maxpositive=0
    localpositive = 0
    minnum=0
    maxnum=0

    for index in range(len(data)-1):

        if data[index]<data[index+1]:
            localpositive+=1
        else:
            localpositive=0
        if localpositive>maxpositive:
            maxpositive=localpositive
            maxnum=data[index+1]
            minnum=data[index+1-maxpositive]

            print(index)
    return maxpositive+1,localpositive,minnum,maxnum
print(
    zad53(diary)
)

