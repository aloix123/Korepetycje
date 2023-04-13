def readData():
    with open("ciagi.txt", "r") as seires:
        x1 = [x.strip() for x in seires.readlines()]
    return x1


data = readData()


def isW1W2eguall(line):
    return line[:len(line) // 2] == line[len(line) // 2:]


def zad1(data):
    resultcount = 0
    for line in data:
        if isW1W2eguall(line):
            resultcount += 1
            print(line)
    return resultcount
def chechneighboursOnes(line):
    if line[0]==1 and line[1]==1:
        return False
    for index in range(1,len(line)-1):
        if

print(zad2(data))
