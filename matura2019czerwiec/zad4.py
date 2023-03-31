def ReadData():
    with open("liczby.txt") as numbers:
        x1=[int(x) for x in numbers.readlines()]
    with open("liczby_przyklad.txt") as examplenumbers:
        x2=[int(x) for x in examplenumbers.readlines()]
    with open("pierwsze.txt") as first:
        x3=[int(x) for x in first.readlines()]
    with open("pierwsze_przyklad.txt") as numbersexample:
        x4=[int(x) for x in numbersexample.readlines()]
    return (x1,x2,x3,x4)
nums,exnums,first,firstexam=ReadData()
def isprime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
def isREversePrime(num):
    return isprime(int(str(num)[::-1]))
def zad1(numbers):
    result=[]
    for number in numbers:
        if  number >=100 and number <=5000 and isprime(number):
            result.append(number)

    return result
def zad2(primes):
    resultTab=[]
    for num in primes:
        if isREversePrime(num):
            resultTab.append(num)
    return resultTab
def Test():

    assert zad1(exnums)==[103, 163, 173, 701, 1033, 2137,3529, 4933, 977, 2143]
    assert zad2(firstexam)==[701,709, 1033, 167, 1109, 1619, 1009, 179, 1499, 76001, 1601, 31873]
    assert checkNumberWeight(31699)==1

    print("tesyt OK")
def checkNumberWeight(num):
    newnum=0
    for digit in str(num):
        newnum+=int(digit)

    if newnum<10:
        return newnum
    else:
        return  checkNumberWeight(newnum)
def zad3(numbers):
    resultcount=0
    resultlist=[]
    for num in numbers:
        if checkNumberWeight(num)==1:
            resultcount+=1
            resultlist.append(num)
    return resultcount,resultlist
Test()
print(zad1(nums))
print(zad2(first))
print(zad3(first))