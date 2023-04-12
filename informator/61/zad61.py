def readData():
    with open("ciagi.txt","r") as data:
        x1=[list(map(int,x.split())) for x in data.readlines()]
    with open("bledne.txt","r") as mistake:
        x2=[list(map(int,x.split())) for x in mistake.readlines()]
    return x1,x2
data,mistake=readData()
def  isSeries(numlist):
    r=numlist[1]-numlist[0]
    for index in range(len(numlist)-1):
        if numlist[index+1]-numlist[index]!=r:
            return [False,r]
    return [True,r]

def zad1(data):
    maxr=0
    seriescount=0
    for lineindex in range(1,len(data),2):
        if isSeries(data[lineindex])[0]:
            seriescount+=1
            maxr=max(maxr,isSeries(data[lineindex])[1])
    return (maxr,seriescount)
def zad2(data):
    squarelist=[x*x*x for x in range(1,101)]

    with open("wynik2","w") as result2:
        for lineindex in range(1,len(data),2):
            maxsquare=0
            for element in data[lineindex]:
                if element in squarelist:
                    maxsquare=max(maxsquare,element)
            if maxsquare!=0:

                result2.write(str(maxsquare)+"\n")
def returnDominantR(series):
    Rlist=[]
    for index in range(len(series)-1):
        Rlist.append(series[index+1]-series[index])
    SetRList=set(Rlist)
    resultR=0
    x1=0

    for element in SetRList:
        if x1<Rlist.count(element):
            x1=Rlist.count(element)
            resultR=element
    diffrentnumber=element
    for numberindex in range(len(series)-1):
        if numberindex==0 and resultR!=series[numberindex+1]-series[numberindex]:
            return (series, series[numberindex ])
        if resultR!=series[numberindex+1]-series[numberindex] :
            return (series,series[numberindex+1])
def zad3(data):
    for index in range(1,len(data),2):
        print(returnDominantR(data[index]))
print(zad3(mistake))

