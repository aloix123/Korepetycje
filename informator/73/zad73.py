def readData():
    with open("tekst.txt","r") as tekst:
        data=tekst.readline().split()
    return data
text=readData()
def zad1(data):
    resultcount=0
    for word in data:
        for leterindex in range(len(word)-1):
            if word[leterindex]==word[leterindex+1]:
                resultcount+=1
                break
    return resultcount
def zad2(data):
    lettercount=0
    for word in data:
        lettercount+=len(word)
    diffrentwords=[]
    for line in data:
        for letter in line:
            diffrentwords.append(letter)
    diffrentwords=set(diffrentwords)
    letterdict={}
    for x in diffrentwords:
        letterdict[x]=0
    for line in data:
        for letter in line:
            letterdict[letter]+=1
    letterdict["Z"]=0
    for g in sorted(letterdict.keys()):
        print(g,letterdict[g],f"{round(letterdict[g]*100/lettercount,2)}%")
def zad3(data):
    longestwunderword=0
    underWordList=[]
    for word in data:
        localcount=0
        for letter in word:
            if letter not in { "A", "E", "I", "O", "U","Y"}:
                localcount+=1
            else:
                localcount=0
            if longestwunderword == localcount:
                underWordList.append(word)
            if longestwunderword<localcount:
                longestwunderword=localcount
                underWordList=[word]

    return underWordList[0],longestwunderword,len(set(underWordList))



print(zad3(text))
