def readData():
    with open("dane_systemy1.txt","r") as data1:
        x1=[list(map(int,x.split())) for x in data1.readlines()]
    with open("dane_systemy2.txt","r") as data2:
        x2=[list(map(int,x.split())) for x in data2.readlines()]
    with open("dane_systemy3.txt","r") as data3:
        x3=[list(map(int,x.split())) for x in data3.readlines()]
    return (x1,x2,x3)
binaryData,fourthData,eightdata=readData()
def changeNUmberFromBinaryToDecent(num):
    return bin(num)