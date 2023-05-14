def readData():
    with open("szyfr1.txt","r") as x1:
        y1=[x.split() for x in x1.readlines()]
    with open("szyfr2.txt", "r") as x2:
        y2 = [x.split() for x in x2.readlines()]
    with open("szyfr3.txt", "r") as x3:
        y3 = [x for x in x3.readlines()]
    return y1,y2,y3
data1,data2,data3=readData()
def encryptword(word,crypt):
    resultword=[]
    for letter in word[0]:
        resultword.append(letter)
    crypt=crypt*len(resultword)

    for wordindex in range(len(resultword)):
        p=resultword[wordindex]
        g=resultword[int(crypt[wordindex])-1]

        resultword[wordindex]=g
        resultword[int(crypt[wordindex]) - 1]=p
    result=""
    for letter in resultword:
        result+=letter
    return result
def uncryprword(word,crypt):

    resultword = []
    for letter in word[0]:
        resultword.append(letter)
    crypt = crypt * len(resultword)


    for wordindex in range(len(resultword)-1,-1,-1):
        p = resultword[wordindex]
        g = resultword[int(crypt[wordindex]) - 1]

        resultword[wordindex] = g
        resultword[int(crypt[wordindex]) - 1] = p
    result = ""
    for letter in resultword:
        result += letter
    return result
def zad1(data):
    for i in range(6):
        print(encryptword(data[i],data[-1]))
def zad2(data):

    print(encryptword(data[0],data[-1]))
def zad3(data):
    print(uncryprword(data[0],[6, 2, 4, 1, 5, 3]))
print(zad3((data3,[6, 2, 4, 1, 5, 3])))




