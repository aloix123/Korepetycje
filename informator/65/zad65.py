def readData():
    with open("dane_ulamki.txt") as nums:
        x1=[list(map(int,x.split())) for x in nums.readlines()]
    return x1
data=readData()
def zad1(data):
    smallestnum=9999999999
    mianownik=99999999999
    licznik=0
    for number in data:
        if number[0]/number[1]<smallestnum:
            smallestnum=min(number[0]/number[1],smallestnum)
            mianownik = number[1]
            licznik = number[0]
        if number[1]/number[0]==smallestnum:
            mianownik=min(mianownik,number[1])
            licznik=number[0]
    return licznik,mianownik
def NWD(a,b):
    if b!=0:
        return NWD(b,a%b)
    return a
def zad2(data):
    resultcount=0
    for number in data:
        if NWD(number[1],number[0])==1:
            resultcount+=1

    return resultcount
def zad3(data):
    resultcount = 0
    for number in data:
        if NWD(number[1], number[0]) == 1:
            resultcount += number[0]
        elif number[0]/number[1]==int(number[0]/number[1]):
            resultcount+=int(number[0]/number[1])
        else:
            resultcount+=number[0]/NWD(number[0],number[1])
    return resultcount
def zad4(data):
    bignum=(3**2)*(2**2)*(5**2)*(7**2)*13
    print(bignum)
    numberSum=0
    for element in data:
        numberSum+=(bignum*(element[0]/element[1]))
    return numberSum
print(zad4(data))