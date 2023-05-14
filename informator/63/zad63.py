def readData():
    with open("ciagi.txt", "r") as seires:
        x1 = [x.strip() for x in seires.readlines()]
    return x1


data = readData()


def isW1W2eguall(line):
    return line[:len(line) // 2] == line[len(line) // 2:]


def zad1(data):
    resultcount = 0
    for line in data:
        if isW1W2eguall(line):
            resultcount += 1
            print(line)
    return resultcount
def chechneighboursOnes(line):
    if line[0]=='1' and line[1]=='1':
        return False
    for index in range(1,len(line)-1):
        if line[index]=='1':
            if line[index-1]=='1' or line[index+1]=='1':
                return False
    return True
def zad2(data):
    resultcount=0
    for line in data:
        if chechneighboursOnes(line):
            resultcount+=1
            print(line)
    return resultcount
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
def isHalfPrime(num):

     num1=int(f"0{num}",2)
     
     i=2
     factors=[]
     while i*i<=num1:
         if num1%i==0:
             factors.append(i)
             num1//=i
         else:
             i+=1
     if num1>1:
         factors.append(num1)

     return len(factors)==2 and isPrime(factors[0]) and isPrime(factors[1])
def zad3(data):
    halfPrimeCount=0
    biggsethalfnum=0
    smallesthalfprime=99999999999999
    for line in data:
        if isHalfPrime(line):
            halfPrimeCount+=1
            biggsethalfnum=max(int(f"0{line}",2),biggsethalfnum)
            smallesthalfprime=min(int(f"0{line}",2),smallesthalfprime)
    return (halfPrimeCount,biggsethalfnum,smallesthalfprime)
print(zad3(data))
