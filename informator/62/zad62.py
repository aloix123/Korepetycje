def readData():
    with open("liczby1.txt","r") as nums1:
        x1=[int(x) for x in nums1.readlines()]
    with open("liczby2.txt","r") as nums2:
        x2=[int(x) for x in nums2.readlines()]
    return (x1,x2)
data1,data2=readData()
def zad1(data):
    samllestNum=9999999
    biggestNum=0
    for number in data:
        samllestNum=min(number,samllestNum)
        biggestNum=max(number,biggestNum)
    return (biggestNum,samllestNum)
def zad2(data):
    seriescount=1
    firstnum=0
    localseriescount=1
    for lineindex in range(len(data)-1):

        if data[lineindex]<=data[lineindex+1]:
            localseriescount+=1
            if localseriescount>seriescount:
                seriescount=localseriescount
                firstnum=data[lineindex-seriescount+1]
        else:
            localseriescount=0
    return (firstnum,seriescount+1)
def zad3a(data1,data2):
    sameNumCount=0
    for i in range(len(data2)):
        if int(oct(data2[i])[2:])==data1[i]:
            sameNumCount+=1
    return sameNumCount
def zad3b(data1,data2):
    biggercount = 0
    for i in range(len(data2)):
        if int(oct(data2[i])[2:]) <data1[i]:
            biggercount += 1
    return biggercount
def zad4(data):
    sixcountdec=0
    sixcountoct=0
    for number in data:
        for digit in str(number):
            if int(digit)==6:
                sixcountdec+=1
        for digitt in str(oct(number)[2:]):
            if int(digitt)==6:
                sixcountoct+=1
    return (sixcountdec,sixcountoct)
print(zad4(data2))



