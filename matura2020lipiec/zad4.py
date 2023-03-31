def readData():
    with open("identyfikator.txt") as identity:
        x=[x.strip() for x in identity.readlines()]
    with open("identyfikator_przyklad.txt") as exidentity:
        y=[x.strip() for x in exidentity.readlines()]
    return (x,y)
identity,example=readData()
def getSUmOfNumbersFromIdentity(id):
    result=0
    for digit in id[3:]:
        result+=int(digit)
    return result
def zad1(identity):
    maxsum=0
    maxfragment=""
    for fragment in identity:
        if getSUmOfNumbersFromIdentity(fragment)>maxsum:
            maxsum=getSUmOfNumbersFromIdentity(fragment)
            maxfragment=fragment
    return maxfragment
def ifPartIsPalindrom(fragment):
    f1=fragment[0:3]
    f2=fragment[3:]
    if f1==f1[::-1] or f2==f2[::-1]:
        return True
    else:
        return False
def zad2(identity):
    result=[]
    for fragment in identity:
        if ifPartIsPalindrom(fragment):
            result.append(fragment)
    return result

def getValueFromFragment(fragment):
    resultvalue=[]
    for i in range(3):
        resultvalue.append(ord(fragment[i])-55)
    resultvalue.append("-")
    for i in range(4,9):
        resultvalue.append(int(fragment[i]))
    return resultvalue
def getweightFromFragment():
    return [7,3,1,"-",7,3,1,7,3]
def multyplication(fragment):
    weight=getweightFromFragment()
    value=getValueFromFragment(fragment)

    controlnum=fragment[3]
    sum=0
    for i in range(len(weight)):
        if weight[i]!="-":

            sum=sum+(value[i]*weight[i])

    if sum%10==int(controlnum):
        return True
    return False

def zad3(identity):
    resultlist=[]
    for fragment in identity:
        if multyplication(fragment)==False:
            resultlist.append(fragment)
    return resultlist
def answers():
    print(zad1(identity))
    print(zad2(identity))
    print(zad3(identity))

def Test():
    assert zad1(example)=="CHY728985"
    assert ifPartIsPalindrom("101abcs")==True
    assert ifPartIsPalindrom("421abba") == True

    #assert print(zad2(example))


answers()
Test()
