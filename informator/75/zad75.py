def readData():
    with open("tekst.txt","r") as words:
        x=[y.split() for y in words.readlines()]
    with open("probka.txt","r") as test:
        h=[g.split() for g in test.readlines()]
    return (x,h)
words,test=readData()
def isDinStartAndEnd(word):
    return word[0]=="d" and word[-1]=="d"
def zad1(data):
    resultcount=0
    for line in data[0]:
        if isDinStartAndEnd(line):
            resultcount+=1
            print(line)
    return resultcount
def zad2(data,A,B):
    for line in data[0]:
        if len(line)>=10:
            fragmentList=[]

            for element in line:
                fragmentList.append(element)

            for i in range(len(fragmentList)):

                fragmentList[i]=ord(fragmentList[i])-97
            for i in range(len(fragmentList)):
                fragmentList[i]=(fragmentList[i]*A)+B
                while fragmentList[i]>25:
                    fragmentList[i]=fragmentList[i]%26
                fragmentList[i]=chr(fragmentList[i]+97)
            stringresult=""
            for part in fragmentList:
                stringresult+=part
            print(stringresult)
def zad3(data):
    for line in data:

        for Aindex in range(0,26):

            for Bindex in range(0, 26):
                localcounr = 0
                for letterindex in range(0,len(line[0])):
                    if line[1][letterindex]==chr(((ord(line[0][letterindex])-97)*Aindex+Bindex)%26+97):
                        localcounr+=1
                if localcounr==len(line[0]):

                    print(f"{Aindex},{Bindex} szyfr")
        for Aindex in range(0,26):

            for Bindex in range(0, 26):
                localcounr = 0
                for letterindex in range(0,len(line[0])):
                    if line[0][letterindex]==chr(((ord(line[1][letterindex])-97)*Aindex+Bindex)%26+97):
                        localcounr+=1
                if localcounr==len(line[0]):

                    print(f"{Aindex},{Bindex} deszyfr")



print(zad3(test))
