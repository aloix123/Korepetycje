
def openfiles():

    with open("liczby.txt","r") as f :
        x=[int(q.strip()) for q in f.readlines()]
    with open("przyklad.txt","r") as g :
        y=[int(c.strip()) for c in g.readlines()]
    return (x,y)
numbers,example=openfiles()


def If17DivideNumber(num):
    if num%17==0:
        return True
    else:
        return False
def Test():

    assert zad41(example)==[51]

    assert zad42(example) == (741 ,594)
    assert isPrime(7)==True
    assert isPrime(8)==False

    assert zad43(example)==[13,131]
def setOppositNumber(num):
    return int(str(num)[::-1])
def zad41(nums):
    oppositenumbers=[]
    for num in nums:
        oppositenumbers.append(setOppositNumber(num))
    resultlist=[]
    for n in oppositenumbers:
        if If17DivideNumber(n):
            resultlist.append(n)
    return resultlist
def differencTwoNums(num1):
    diffenerce=num1-setOppositNumber(num1)
    if diffenerce<0:
        return -diffenerce
    else:
        return diffenerce
def zad42(numbers):
    maxnum=0
    maxdifference=0
    oppositenums=[]
    for num in numbers:
        if differencTwoNums(setOppositNumber(num))>maxdifference:
            maxnum=num
            maxdifference=differencTwoNums(setOppositNumber(num))
    return (maxnum,maxdifference)
def isPrime(num):
    i=2

    while i*i<=int(num):
        if num%i==0:
            return False

        i+=1
    return True

def zad43(numbers):
    result=[]
    for number in numbers:
        if isPrime(number) and isPrime(setOppositNumber(number)):
            result.append(number)
    return result
def zad44(numbers):
    print(len(numbers)-len(set(numbers)))
    dykta={}
    for x in set(numbers):
        dykta[x]=0
    for n in numbers:

        dykta[n]+=1
    result=[]
    print(dykta)
    for g in range(max(dykta.keys())):
        if dykta.get(g)==3 :
            result.append(g)
    print(result)


Test()
print(zad41(numbers))
print(zad42(numbers))
print(zad43(numbers))
print(zad44(numbers))