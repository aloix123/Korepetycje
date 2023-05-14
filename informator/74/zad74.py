def readData():
    with open("hasla.txt","r") as data:
        x=[x.strip() for x in data.readlines()]
    return x
data=readData()
def zad1(passwords):
    nums=[str(x) for x in range(0,10)]
    resultcount=0
    for line in passwords:
        indexcount=0
        for element in line:
            if element  in nums:
                indexcount+=1
        if indexcount==len(line):
            resultcount+=1
    return resultcount
def zad2(passwords):
    for firstindex in range(len(passwords)):
        for secindex in range(firstindex+1,len(passwords)):
            if passwords[firstindex]==passwords[secindex]:
                print(passwords[firstindex])
                break
    return 0
def zad3(passwords):
    resultcount=0
    for line in passwords:

        for index in range(len(line)-3):
            localist=[]
            localist.append(ord(str(line[index])))
            localist.append(ord(str(line[index+1])))
            localist.append(ord(str(line[index+2])))
            localist.append(ord(str(line[index+3])))
            localist=sorted(localist)
            if localist[0]+1==localist[1] and localist[1]+1==localist[2] and localist[2]+1==localist[3]:
                resultcount+=1
                break
def zad4(passwords):
    alldigits=[str(x)for x in range(10)]
    print(alldigits)
    resultcount=0
    for line in passwords:
        flag1=False
        flag2=False
        flag23=False
        for element in line:
            if element in alldigits:
                flag1=True
            elif element.lower()==element:
                flag2=True
            elif element.upper()==element:
                flag23=True
        if flag1 :
            if flag2:
                if flag23:
                    resultcount+=1
    return resultcount







print(zad4(data))
