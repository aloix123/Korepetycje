def readData():
    with open("liczby.txt","r") as nums:
        x1=[int(x) for x in nums.readlines()]
    return x1
numbers=readData()
print(numbers)
def issmallerThan1000(num):
    return num<1000
def zad1(data):
    result=0
    numlist=[]
    for line in data:
        if issmallerThan1000(line):
            result+=1
            numlist.append(line)
    lastwonums=(numlist[-1],numlist[-2])
    return lastwonums,result
def checkNumFactors(num):
    i=1
    factors=[]
    while i<=num/2+1:
        if num%i==0:

            factors.append(i)

        i+=1
    if num>1:
        factors.append(num)

    return [num,factors,len(factors)]
def zad2(data):

    for element in data:
        lineinf=checkNumFactors(element)
        if lineinf[2]==18:
            print(lineinf[0])
            print(lineinf[1])
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
def isPrime(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:

            return False
        i+=1

    return True
def zad3(data):
    result=0
    for index1 in range(len(data)):
        d=0
        for  index2 in range(len(data)):
            if nwd(data[index1],data[index2])!=1 and data[index1]!=data[index2]:
                d+=1
        if d==0:
            if result<data[index1]:
                result=data[index1]

    return result

print(zad3(numbers))