def readData():
    with open("dane_napisy.txt","r") as data:
        x=[list(x.split()) for x in data.readlines()]
    return x
data=readData()
def isAnagram(word1,word2):
    list1=[0 for x in range(25)]
    list2=[0 for x in range(25)]
    for digit in word1:
        list1[ord(digit)-65]+=1
    for digit in word2:
        list2[ord(digit) - 65] += 1
    for index in range(len(list1)):
        if list1[index]!=list2[index]:
            return False
    return True
def zad1(data):
    resultcount=0
    for line in data:
        if isAnagram(line[0],line[1]) and len(set(line[0]))==1:
            resultcount+=1
    return resultcount
def zad2(data):
    resultcount=0
    for line in data:
        if isAnagram(line[0],line[1]):
            resultcount+=1
    return resultcount
def zad3(data):
    resultlist=[]
    locallist=[]
    resultcount=0
    localcount=0
    for index in range(len(data)):
        if isAnagram(data[index][0],data[index][1]):
            localcount+=1
            for element in range(index,len(data)):
                for part in [0,1]:
                    if isAnagram(data[index][0],data[element][part]):
                        localcount+=1
                        locallist.append(data[element][part])
            if localcount>resultcount:
                resultcount=localcount
                resultlist=locallist
            locallist=[]
            localcount=0
    return len(resultlist)
print(zad3(data))