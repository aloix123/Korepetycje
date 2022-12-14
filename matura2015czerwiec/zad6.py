def openfile():
    with open("kody.txt","r") as file :
        x=[x.strip() for x in file.readlines()]
    return x
def openzad1():
    with open("kody1.txt","r") as file :
        x=[x.strip() for x in file.readlines()]
    return x
def openzad2():
    with open("kody2.txt","r") as file :
        x=[x.strip() for x in file.readlines()]
    return x
kody=openfile()
def zad61(nums):
    resultparzystanum=[]
    nieparzystasum=[]
    with open("kody1.txt","w") as filezad1:
        for number in nums:
            odd=0
            even=0
            for num in range(1,len(number),2):
                odd+=int(number[num])
            for num in range(0,len(number),2):
                even+=int(number[num])
            filezad1.write(f"{odd} {even}")
            filezad1.write("\n")
kody1=openzad1()
kody2=openzad2()

def calkulatedigit(file1):
    resultlist=[]
    for twonums in file1:
        num1,num2=twonums.split()
        sum=3*int(num1)+int(num2)
        restofnum=sum%10
        finalnum=(10-restofnum)%10

        resultlist.append(finalnum)
    return resultlist
numdict={0 :10101110111010,
1 :11101010101110,
2 :10111010101110,
3 :11101110101010,
4 :10101110101110,
5 :11101011101010,
6 :10111011101010,
7 :10101011101110,
8: 11101010111010,
9: 10111010111010 }
def zad62(file):
    numdict = {0: '10101110111010',
               1: '11101010101110',
               2: '10111010101110',
               3: '11101110101010',
               4: '10101110101110',
               5: '11101011101010',
               6: '10111011101010',
               7: '10101011101110',
               8: '11101010111010',
               9: '10111010111010'}
    with open("kody2.txt","w") as kody2file:
        for number in file:

            kody2file.write(f"{number} {numdict[number]} \n")



zad62(calkulatedigit(kody1))

def zad63(filezad2,filekody):
    numdict = {0: '10101110111010',
               1: '11101010101110',
               2: '10111010101110',
               3: '11101110101010',
               4: '10101110101110',
               5: '11101011101010',
               6: '10111011101010',
               7: '10101011101110',
               8: '11101010111010',
               9: '10111010111010'}
    start="11011010"
    stop="11010110"
    with open("kody3.txt","w") as kody3file:
        cebula1=[]
        cebula2=[]
        for x in  filekody:
            for digit in x:
                cebula1.append([x[0],x[1],x[2],x[3],x[4],x[5]])
        for y in filezad2:
            num,code=y.split()
            cebula2.append([num,code])
        for i in range(len(cebula1)):

            finalstring=f"{start}{numdict[int(cebula1[i][0])]}{numdict[int(cebula1[i][1])]}{numdict[int(cebula1[i][2])]}{numdict[int(cebula1[i][3])]}{numdict[int(cebula1[i][4])]}{numdict[int(cebula1[i][5])]}{cebula2[i][1]}{stop}\n"
            kody3file.write(finalstring)

zad63(kody2,kody)

