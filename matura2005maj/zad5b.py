def readfiles():
    with open("dane5-1.txt","r")as dane1:
        x1=[int(x.strip()) for x in dane1]
    with open("dane5-2.txt","r")as dane2:
        x2=[int(x.strip()) for x in dane2]
    with open("dane5-3.txt","r")as dane3:
        x3=[int(x.strip()) for x in dane3]
    return(x1,x2,x3)
data1,data2,data3=readfiles()
def getmaxsum(data):
    maxnum=0
    maxresult=0
    for num in data:
        maxnum+=num
        if maxnum>maxresult:
            maxresult=maxnum
        if maxnum<0:
            maxnum=0
    return maxresult
def zadB(d1,d2,d3):
    print(f"dane1 {getmaxsum(d1)}")
    print(f"dane2 {getmaxsum(d2)}")
    print(f"dane3 {getmaxsum(d3)}")
    return 0
zadB(data1,data2,data3)