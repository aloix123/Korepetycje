def readData():
    with open("liczby.txt","r") as nums:
        x=[x.strip() for x in nums.readlines()]
    return x
data=readData()
def isOctal(num):
    return 8==int(num[-1])
def isfourtal(num):
    return 4==int(num[-1])
def isbinary(num):
    return 2==int(num[-1])

def isEven(num):
    if isbinary(num):
        return int(f"0{num[:-1]}",2)%2==0
def zad1(numbers):
    octalcount=0
    for num in numbers:
        if isOctal(num):
            octalcount+=1
    return octalcount
def zad2(numbers):
    fourcount=0
    for num in numbers:
            if isfourtal(num) and "0" not in num:
                fourcount+=1
    return fourcount
def zad3(numbers):
    resultcount=0
    for num in numbers:
        if isEven(num) :
            resultcount+=1
    return resultcount
def zad4(numbers):
    resultsum=0
    for num in numbers:
        if isOctal(num):
            resultsum+=int(f"0{num[:-1]}",8)
    return resultsum
def NumValue(num):
    return int(f"0{num[:-1]}",int(num[-1]))
def zad5(numbers):
    minnumcode=""
    maxnumcode=""
    decnumMin=NumValue(numbers[0])
    decnumMax=NumValue(numbers[0])
    for num in numbers:
        decnum=NumValue(num)
        if decnum>decnumMax:
            decnumMax=decnum
            maxnumcode=num
        elif decnum<decnumMin:
            decnumMin=decnum
            minnumcode=num
    return (f"najmniejsza to {minnumcode} a w dziesiętnym jest {decnumMin}",f"natomiast najwiękrza to {maxnumcode} i w dziesiętnym jes równa {decnumMax}")



print(zad1(data))
print(zad2(data))
print(zad3(data))
print(zad4(data))
print(zad5(data))