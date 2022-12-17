def readfiles():
    with open("dane1.txt","r")as dane1:
        d1=[list(map(int,x.split())) for x in dane1.readlines()]
    with open("dane2.txt","r")as dane2:
        d2=[list(map(int,x.split())) for x in dane2.readlines()]
    with open("przyklad1.txt","r")as daneprz1:
        d3=[list(map(int,x.split())) for x in daneprz1.readlines()]
    with open("przyklad2.txt","r")as daneprz2:
        d4=[list(map(int,x.split())) for x in daneprz2.readlines()]
    return (d1,d2,d3,d4)
data1,data2,exampledata1,exampledata2=readfiles()
def TEST():
    assert zad41(exampledata1,exampledata2)==3
    assert zad42(exampledata1,exampledata2)==1
    assert zad43(exampledata1,exampledata2)=="1,5"

    print("TESTY OK")
def zad41(file1,file2):
    result=0
    for i in range(len(file1)):
        if file2[i][-1]==file1[i][-1]:
            result+=1
    return result
def zad42(file1,file2):
    result=0
    for i in range(len(file1)):
        xeven1=0
        xodd1=0
        for num1 in file1[i]:
            if num1%2==0:
                xeven1+=1
            else:
                xodd1+=1
        xeven2=0
        xodd2=0
        for num2 in file2[i]:
            if num2%2==0:
                xeven2+=1
            else:
                xodd2+=1
        if xodd2>=5 and xodd1>=5 and xeven1>=5 and xeven2>=5:
            result+=1

    return result
def zad43(file1,file2):
    result=[]
    for i in range(len(file1)):
        if set(file1[i])==set(file2[i]):
            result.append(i)
    finalstring=""
    for num in result:
        finalstring+=str(num+1)+","
    return finalstring[:-1]
def zad44(file1,file2):
    with open("wynik4_4.txt ","w") as wynik4:
        for i in range(len(file1)) :
            f1=0
            f2 = 0
            result = []
            while f1<len(file1[i]) and f2<len(file1[i]):




                print(f1,f2)
                if file1[i][f1]==file2[i][f2]:
                    result.append(file2[i][f2])
                    result.append(file1[i][f1])
                    f2+=1
                    f1+=1
                elif file1[i][f1]>file2[i][f2]:
                    result.append(file2[i][f2])
                    f2+=1
                elif file1[i][f1]<file2[i][f2]:
                    result.append(file1[i][f1])
                    f1 += 1
                if f1==len(file1):
                    for y in  range(f2-1,len(file1)+1):
                        result.append(file2[i][y])
                    break
                elif f2==len(file2):
                    for x in  range(f1-1,len(file1)+1):
                        result.append(file1[i][x])
                    break
            finalstring=""
            for num in result:
                finalstring+=str(num)+" "
            wynik4.write(finalstring[:-1]+"\n")


TEST()

print(zad41(data1,data2))
print(zad42(data1,data2))
print(zad43(data1,data2))

zad44(data1,data2)