def readData():
    with open("liczby.txt") as numbers:
        x1=[int(x) for x in numbers.readlines() ]
    return x1
nums=readData()
def excahngeNum(num):
    result=0
    for digit in str(num):
        result+=int(digit)**2
    return result
def isHappyNumber(num):
    newnum=excahngeNum(num)
    resultnum = []
    while num!=newnum and newnum!=1 and newnum not in resultnum:
        resultnum.append(newnum)
        newnum=excahngeNum(newnum)

    if newnum==1:
        return True
    if newnum==num:
        return False
def modyfIsHappynumber(num):
    newnum = excahngeNum(num)
    resultnum=[]
    while num != newnum and newnum != 1 and newnum not in resultnum:
        resultnum.append(newnum)
        newnum = excahngeNum(newnum)

    if newnum == 1:
        return resultnum
    if newnum == num:
        return False

def zad1():
    resulthappycount=0
    resulthappylist=[]
    happynums=[]
    for number in range(2,1001):

        if isHappyNumber(number):
            if len(modyfIsHappynumber(number))>resulthappycount:
                resulthappylist.clear()
                resulthappycount=len(modyfIsHappynumber(number))
                resulthappylist.append(number)
            if len(modyfIsHappynumber(number))>=resulthappycount:

                resulthappycount=len(modyfIsHappynumber(number))
                resulthappylist.append(number)
    return resulthappycount+2,resulthappylist
def zad2(nums):
    happyCount=0
    for number in nums:
        if isHappyNumber(number):
            happyCount+=1
    return happyCount
def zad3(nums):
    resultciąg=0
    numindex=0
    ciąg=0
    happyindex=0

    for index in range(len(nums)):
        if ciąg>resultciąg:
            resultciąg=ciąg
            numindex=index
        if happyindex==index:
            ciąg+=1
        else:
            ciąg=0
        if isHappyNumber(nums[index]):
           happyindex=index+1
    firsthapy = nums[numindex-resultciąg-1]
    lasthappy = nums[numindex-2]


    return resultciąg,firsthapy,lasthappy
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
print(isPrime(17))
def isHappyAndPrime(num):
    return isHappyNumber(num) and isPrime(num)
def zad4(numbers):
    result=0
    for num in numbers:
        if isHappyAndPrime(num):
            result+=1
    return result
print(zad1())
print(zad2(nums))
print(zad3(nums))
print(zad4(nums))