def readFiles():
    with open("dane_6_1.txt","r") as file1:
        dane1=[x.strip() for x in file1.readlines()]
    with open("dane_6_2.txt","r") as file2:
        dane2=[list(x.split()) for x in file2.readlines()]
    with open("dane_6_3.txt","r") as file3:
        dane3=[list(x.split()) for x in file3.readlines()]
    return (dane1,dane2,dane3)
dane1,dane2,dane3=readFiles()
k=107
def codeWord(word,key):
    newWord=""
    for letter in word:
        indexletter=ord(letter)+key
        while indexletter>90:
            indexletter-=26


        newWord+=chr(indexletter)
    return newWord
def unCodeWord(word):
    newWord = ""
    if len(word)==1:
        return word[0]

    word[1]=int(word[1])%26

    for letter in word[0]:

        indexletter=ord(letter)-word[1]
        while indexletter<65:
            indexletter+=26
        while indexletter>90:
            indexletter-=25

        newWord += chr(indexletter)
    return newWord
def checkIfSmaeKey(letter1,letter2):
    mainkey = ord(letter2[0]) - ord(letter1[0])
    if mainkey<0:
        mainkey=-mainkey


    for i in range(len(letter1)):

        key=(ord(letter2[i])%26-ord(letter1[i])%26)
        if key<0:
            key=-key



        if mainkey==key  or 26-key==mainkey:
            pass
        else:
            return False
    return True

def zad61(dane1,key):
    with open("wyniki_6_1.txt", "w") as file:
        for word in dane1:
            file.write(codeWord(word,key)+"\n")
def zad62(dane2):
    with open("wyniki_6_2.txt","w") as file2:
        for i in dane2:
            file2.write(unCodeWord(i)+"\n")
def zad63(dane3):
    with open("wynik_6_3.txt", "w") as file:
        for word in dane3:
            if False== checkIfSmaeKey(word[0],word[1]):
                file.write(f"{word[0]} {word[1]} \n")

zad62(dane2)
zad61(dane1,k)
zad63(dane3)

