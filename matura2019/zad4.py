def readData():
    with open("przyklad.txt") as example:
        x1 = [int(x.strip()) for x in example.readlines()]
    with open("liczby.txt") as nums:
        x2 = [int(x.strip()) for x in nums.readlines()]
    return (x1,x2)
def allResults():
    print(zad1(numbers))
    print(zad2(numbers))

def TEST():
    assert zad1(example) == 2

    assert zad2(example)[0]==145
example,numbers=readData()
def FactorNumber(number):
    if number<1:
        return 1
    else:
        return FactorNumber(number-1)*number

def returnPoweredThree():
    numbers=[1,3]
    index=2
    while numbers[-1]<1_000_000:
        numbers.append(3**index)
        index+=1
    return numbers

def zad1(data):
    allThreePoweredNumbers=returnPoweredThree()
    result=0

    for num in data:

        if num in allThreePoweredNumbers:
            result+=1
    return result
def zad2(data):
    resultlist=[]
    for indexedNumber in data:
        checedNUm=0
        for digit in str(indexedNumber):
            checedNUm+=FactorNumber(int(digit))
        if indexedNumber==checedNUm:
            resultlist.append(indexedNumber)
    return resultlist
def NWD(a,b):
    if a>b:
        a-=b
    if b>a:
        b-=a
    if a==b:
        return a
    
print(NWD(2,6))

TEST()
allResults()

