
import math
def readdata():
    with open("dane4.txt") as data:
        x = [int(f.strip()) for f in data.readlines()]
    return x

numbers = readdata()

def zad1(nums):
    maxdifference = 0
    mindif=float("inf")
    for index in range(len(nums) - 1):
        if abs(nums[index] - nums[index + 1]) >maxdifference:
            maxdifference=abs(nums[index] - nums[index + 1])
        if abs(nums[index] - nums[index + 1]) <mindif:
            mindif= abs(nums[index] - nums[index + 1])
    return maxdifference,mindif
def zad42(nums):
    startregular=0
    maxregular=0
    presentregular=95218071-92024372
    indexregular=0
    endregular=0
    for n in range(len(nums)-1):
        numbergap = abs(nums[n] - nums[n + 1])
        if indexregular>maxregular:
            maxregular=indexregular
            endregular=nums[n]
            startregular=nums[n-maxregular]

        if presentregular==numbergap:

            indexregular+=1
        if presentregular!=numbergap:
            indexregular=0
            presentregular=numbergap
    return startregular,endregular,maxregular+2
def zad43(nums):
    tabcount=[]

    for n in range(len(nums)-1):
        numbergap = abs(nums[n] - nums[n + 1])
        tabcount.append(numbergap)
    setbcount=set(tabcount)
    dictnums={}
    for num in setbcount:
        dictnums[num] = 0
    for num in setbcount:
        for n in tabcount:
            if num==n:
                dictnums[num]+=1
    result=dictnums.items()
    print(max(dictnums.values()))
    for pair in result:
        if pair[1]==31:
            print(pair[0])


    return 0
print(zad1(numbers))
print(zad42(numbers))
zad43(numbers)








