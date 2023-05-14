
def fibonacci(num):
    a=1
    b=1
    c=2
    if num==1:
        return 1
    if num==2:
        return 1
    if num==3:
        return 2
    for i in range(num-3):
        a=b
        b=c
        c=a+b
    return c
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True


def zad1():
    list=[10,20,30,40]
    for element in list:
        print(fibonacci(element))
def createBinrayFiboLine(num):
    biggestnum=102334155
    maxlengh=len(bin(biggestnum)[2:])
    numlengh=len(bin(num)[2:])
    zeroes="0"*(maxlengh-numlengh)
    return f"{zeroes}{bin(num)[2:]}"

def zad2():
    fibolis=[fibonacci(x) for x in range(1,41)]
    for element in fibolis:
        if isPrime(element):
            print(element)
def zad3():
    fibolis=[fibonacci(x) for x in range(1,41)]
    for element in fibolis:
        print(createBinrayFiboLine(element))
def zad4():
    fibolis=[fibonacci(x) for x in range(1,41)]
    for element in fibolis:
        onecount=0
        for digit in createBinrayFiboLine(element):
            if digit=="1":
                onecount+=1
        if onecount==6:
            print(createBinrayFiboLine(element))
zad4()


