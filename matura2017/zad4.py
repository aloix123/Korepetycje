def readData():
    with open("dane.txt") as data:
        x1=[list(map(int,x.split()))for x in data.readlines() ]
    with open("przyklad.txt") as example:
        x2=[list(map(int,x.split()))for x in example.readlines() ]
    return (x1,x2)
import math
data,example=readData()
def zad1(pixels):
    mostshiny=0
    leastshiny=266
    for element in pixels:
        for piece in element:
            if piece>mostshiny:
                mostshiny=piece
            if leastshiny>piece:
                leastshiny=piece
    return mostshiny,leastshiny
def test():
    assert zad1(example)==(255,0)
    assert zad2(example)==3
    print("ok testy")
def isOXPallindrom(line):
    for pieceindex in range(len(line)):

        if line[pieceindex]!=line[-pieceindex-1]:
            return False
    return True
def zad2(pixels):
    result=0
    for line in pixels:
        if  not isOXPallindrom(line):
            result+=1

    return result
def zad3(data):
    result=0
    for index in range(len(data)):
        for indexline in range(data[index]):
            cordy=[(1,0),(-1,0),(0,1),(0,-1)]
            for cord in cordy:
                if indexline+cord[0]>319:
                    pass

test()
print(zad1(data))
print(zad2(data))