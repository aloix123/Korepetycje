def readData():
    with open("trojki.txt","r") as nums:
        x=[list(map(int,x.split())) for x in nums.readlines()]
    return x
data=readData()
def ifDigitSumEqLast(numdata):
    lastnum=numdata[2]
    sumnum=0
    for element in range(len(numdata)-1):
        for digit in str(numdata[element]):
            sumnum+=int(digit)

    return lastnum==sumnum
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1

    return True
def zad1(numbers):
    for line in numbers:
        if ifDigitSumEqLast(line):
            print(f"{line[0]} {line[1]} {line[2]}")
def zad2(numbers):
    for line in numbers:
        if isPrime(line[0]) and isPrime(line[1]) and line[0]*line[1]==line[2]:
            print(f"{line[0]} {line[1]} {line[2]}")
def zad3(numbers):
    for line in numbers:
        if line[0]**2+line[1]**2==line[2]**2 or  line[0]**2+line[2]**2==line[1]**2 or line[2]**2+line[1]**2==line[0]**2:
            print(f"{line[0]} {line[1]} {line[2]}")
def zad4(numbers):
    resultcount=0
    resultseries=0
    localcount=0
    for line in numbers:
        if line[0]+line[1]>line[2] and line[1]+line[2]>line[0] and line[0]+line[2]>line[1]:
           resultcount+=1
           localcount+=1
        else:
            localcount=0
        resultseries=max(resultseries,localcount)
    return resultcount,resultseries


print(zad4(data))