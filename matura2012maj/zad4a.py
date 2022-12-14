def readfiles():
    with open("tj.txt","r") as words:
        t=[x.strip() for x in words.readlines()]
    with open("klucze1.txt","r") as keys:
        k=[x.strip() for x in keys.readlines()]
    return (t,k)
def readfilesb():
    with open("sz.txt","r") as words:
        t=[x.strip() for x in words.readlines()]
    with open("klucze2.txt","r") as keys:
        k=[x.strip() for x in keys.readlines()]
    return (t,k)
tj,keys1=readfiles()
sz,keys2=readfilesb()
def codeword(tjword,keyword):

    while len(tjword)>len(keyword):
        keyword+=keyword
    finalword=""
    for letterindex in range(len(tjword)):
        lettersum=ord(tjword[letterindex])+ord(keyword[letterindex])-64
        while lettersum>=90:
            lettersum-=26
        finalword+=chr(lettersum)
    return finalword
def zad4a(examplefile,keyfile):
    with open("wynik4a.txt","w") as wyniki4a:
        for i in range(len(examplefile)):
            wyniki4a.write(codeword(examplefile[i],keyfile[i])+"\n")
def decodeWord(tjword,keyword):
        while len(tjword) > len(keyword):
            keyword += keyword
        finalword = ""
        for letterindex in range(len(tjword)):
            lettersum = ord(tjword[letterindex]) - ord(keyword[letterindex]) +64
            while lettersum >= 90:
                lettersum -= 26
            while lettersum < 65:
                lettersum += 26
            finalword += chr(lettersum)
        return finalword
def zad4a(examplefile,keyfile):
    with open("wynik4b.txt","w") as wyniki4a:
        for i in range(len(examplefile)):
            wyniki4a.write(decodeWord(examplefile[i],keyfile[i])+"\n")
zad4a(tj,keys1)
zad4a(sz,keys2)

