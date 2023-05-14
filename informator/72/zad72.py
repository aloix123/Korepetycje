def readData():
    with open("napisy.txt","r") as words:
        x=[x.split() for x in words.readlines()]
    return x
data=readData()
def zad1(letters):
    resultcount=0
    wordlist=[]
    for wordline in letters:
        if len(wordline[0])/len(wordline[1])>=3 or len(wordline[1])/len(wordline[0])>=3:
            resultcount+=1
            wordlist.append(wordline)
    return wordlist[0][0],wordlist[0][1],resultcount
def zad2(letters):
    for wordline in letters:
        if len(wordline[0])>len(wordline[1]):
            if wordline[0][:len(wordline[1])]==wordline[1]:
                print(wordline[1])
                print(wordline[0][len(wordline[1]):])
        else:
            if wordline[1][:len(wordline[0])] == wordline[0]:
                print(wordline[0])
                print(wordline[1][len(wordline[0]):])

def zad3(letters):
    maxendlist=[]
    maxEndLengh=0
    for wordline in letters:
        localcount=0
        for i in range(-1,-min(len(wordline[0]),len(wordline[1])),-1):
            if wordline[0][i]==wordline[1][i]:
                localcount+=1
            else:
                if maxEndLengh==localcount:
                    maxendlist.append(wordline[0][i:-1])
                    maxendlist.append(wordline[1][i:-1])

                if maxEndLengh<localcount:
                    maxEndLengh=localcount
                    maxendlist=[wordline[0][i:-1],wordline[1][i:-1]]
                localcount=0
    return maxendlist,maxEndLengh
print(zad3(data))
