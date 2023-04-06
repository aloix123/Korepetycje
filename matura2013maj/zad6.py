def readData():
    with open("dane.txt") as data:
        x1=[int(x) for x in data.readlines()]
    return x1
data=readData()
def isLastAndFirstDigitSame(number):
    return str(number)[0]==str(number)[-1]
def zad1(numbers):
    resultcount=0
    for num in numbers:
        if isLastAndFirstDigitSame(num):
            resultcount+=1
    return resultcount
def changefromocttodec(num):
    return int(f'0{num}',8)
def zad2(numbers):
    resultcount = 0
    for num in numbers:
        if isLastAndFirstDigitSame(changefromocttodec(num)):
            resultcount += 1
    return resultcount
def zad3(numbers):
    resultcount=0
    minnum=9999999
    maxnum=0
    for num in numbers:
        flag=True
        for digitindex in range(len(str(num))-1):
            if str(num)[digitindex]>str(num)[digitindex+1]:
                flag=False
        if flag:
            resultcount+=1
            if num<minnum:
                minnum=num
            if num>maxnum:
                maxnum=num

    return resultcount,minnum,maxnum
print(zad1(data))
print(zad2(data))
print(zad3(data))