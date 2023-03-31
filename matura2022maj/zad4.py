def readData():
    with open("liczby.txt","r") as data:
        x=[int(x) for x in data.readlines()]
    with open("przyklad.txt","r") as dataa:
        xy=[int(x) for x in dataa.readlines()]
    return (x,xy)
numbers,example=readData()
print(numbers)
def isLastAndFirstDigitSame(num):
    strnum=str(num)
    if strnum[0]==strnum[-1]:
        return True
    else:
        return False
def defineNumberToNumbers(num):
    i=2
    resultlist=[]
    while i<=num:
        while num%i==0:
            resultlist.append(i)
            num/=i

        i+=1
    return resultlist

def zad1(numbers):
    i=0
    firstnum=0
    for num in numbers:
       if isLastAndFirstDigitSame(num):
           if i==0:
               firstnum=num
           i+=1
    return (i,firstnum)
def zad2(numbers):
    resultmaxlengh=0
    resultnum=0
    resultdiffrentlenghmax=0
    resultdifnum=0
    for num in numbers:
        if len(defineNumberToNumbers(num))>resultmaxlengh:
            resultnum=num
            resultmaxlengh=len(defineNumberToNumbers(num))
        if len(set(defineNumberToNumbers(num)))>resultdiffrentlenghmax:
            resultdifnum=num
            resultdiffrentlenghmax=len(set(defineNumberToNumbers(num)))
    return (resultnum,resultmaxlengh,resultdifnum,resultdiffrentlenghmax)
def zad3(nums):
    threecount=0
    fivecount=0
    numlist=[]
    numfive=[]
    for numindex  in range(len(nums)):
        a=nums[numindex]
        for index1 in range(len(nums)):
            b=nums[index1]
            if b%a==0 and a!=b:
                for index2 in range(len(nums)):
                    c=nums[index2]

                    if c%b==0 and c!=b:
                            numlist.append(f"{a} {b} {c}")
    for numindex  in range(len(nums)):
        a=nums[numindex]
        for index1 in range(len(nums)):
            b=nums[index1]
            if b%a==0 and a!=b:
                for index2 in range(len(nums)):
                    c=nums[index2]

                    if c%b==0 and c!=b:
                        for index3 in range(len(nums)):
                            d = nums[index3]
                            if d % c == 0 and d != c:
                                for index4 in range(len(nums)):
                                    e = nums[index4]
                                    if e % d == 0 and d != e:
                                        numfive.append(f"{a} {b} {c} {d} {e}")

    with open("trojki.txt","w") as three:
        for resulthree in numlist:
            three.write(resulthree+"\n")
    return numfive





def Test():
    assert isLastAndFirstDigitSame(66)
    #print(zad1(example))
    #print(defineNumberToNumbers(420))
    #print(zad2(example))

    #print(zad3(example))
Test()
print(zad1(numbers))
print(zad2(numbers))
print(zad3(numbers))