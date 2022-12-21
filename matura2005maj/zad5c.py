def readfiles():
    with open("dane5-1.txt","r")as dane1:
        x1=[int(x.strip()) for x in dane1]
    with open("dane5-2.txt","r")as dane2:
        x2=[int(x.strip()) for x in dane2]
    with open("dane5-3.txt","r")as dane3:
        x3=[int(x.strip()) for x in dane3]
    return(x1,x2,x3)
data1,data2,data3=readfiles()
def getMostPopular(data):
    sievedict={}
    for num in data:
        sievedict[num]=0
    for num in data:
        sievedict[num]+=1
    maxamount=max(sievedict.values())
    prosto=sievedict.items()
    print(prosto)
    for pair in prosto:
        if pair[1]==maxamount:
            return pair[0]



def zadc(d1,d2,d3):
    print(f"most popular num is {getMostPopular(d1)}")
    print(f"most popular num is {getMostPopular(d2)}")
    print(f"most popular num is {getMostPopular(d3)}")
    return 0
zadc(data1,data2,data3)

