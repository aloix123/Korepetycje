def readData():
    with open("liczby.txt","r") as numbers:
        x1=[int(x) for x in numbers.readlines()]
    return x1
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1

    return True
def convertNumTonums(num):
    i=2
    parts=[]
    while i*i<=num:
        while num%i==0:
            parts.append(i)
            num/=i
        i+=1

    if num>1:
        parts.append(num)
    return parts
def zad1(numbers):
    resultcount=0
    for num in numbers:
        n1=convertNumTonums(num)
        index=0

        if len(set(n1))==3 and (2 not in n1) :
            print(set(n1))
            resultcount+=1
    return resultcount
def TEST():
    assert isPrime(7)==True
    assert isPrime(8)==False
def isPalindrom(num):
    return str(num)[::-1]==str(num)
def zad2(numbers):
    result=0
    for element in numbers:
        x=element+int(str(element)[::-1])
        if isPalindrom(x):
            result+=1
    return result
def checkNumberPower(num,power=0):
    if num<10:
        return power
    newnum=1
    for digit in str(num):
        newnum*=int(digit)
    return checkNumberPower(newnum,power+1)
def zad3(numbers):
    result1=0
    minone=float("inf")
    maxone=0
    dict={}
    for i in range(1,9):
        dict[i]=0

    for line in numbers:
        if checkNumberPower(line)<9:
            dict[checkNumberPower(line)]+=1
            if checkNumberPower(line)==1:
                if line>maxone:
                    maxone=line
                if line<minone:
                    minone=line
    return dict,minone,maxone
TEST()
numbers=readData()

print(zad3(numbers))
