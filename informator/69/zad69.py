def readData():
    with open("dane_geny.txt","r") as data:
        x=[x.strip() for x in data.readlines()]
    return x
genez=readData()
def zad1(data):
    resultcount=0
    specieslenghlist=[]
    for line in data:
        specieslenghlist.append(len(line))
    resultcount=len(set(specieslenghlist))
    longestlengh=0
    type=0
    for element in set(specieslenghlist):
        localcount=specieslenghlist.count(element)
        if localcount>longestlengh:
            longestlengh=localcount
            type=element
    return element,longestlengh,resultcount
def zad2(data):
    resultcount=0
    for line in data:

        genstart=line.find("AA")
        genend=line.find("BB",int(genstart))
        while genstart!=-1 and genend!=-1:
            if "BCDDC" in line[genstart:genend]:
                resultcount+=1
                break
            genstart=line.find("AA",int(genend))
            genend = line.find("BB",int(genstart) )

    return resultcount
def zad3(data):
    resultcount = 0
    maxgenlengh=0
    for line in data:
        localcount=0
        genstart = line.find("AA")
        genend = line.find("BB", int(genstart))
        while genstart != -1 and genend != -1:
            localcount += 1
            maxgenlengh = max(maxgenlengh, genend-genstart+2)
            genstart = line.find("AA", int(genend))
            genend = line.find("BB", int(genstart))

        resultcount=max(resultcount,localcount)
    return resultcount,maxgenlengh
def zad4(data):
    palindromcount=0
    for line in data:
        localcount=0
        genstart = line.find("AA")
        bgenend=line.find("BB", int(genstart))
        genend = line.find("AA", bgenend)
        while genstart!=-1 and genend!=-1 and bgenend!=-1:
            if line[genstart:genend+2]==line[genstart:genend+2:-1]:
                palindromcount+=1
                print(line[genstart:genend+2])
                genstart = line.find("AA", int(genend))
                genend = line.find("BB", int(genstart))
    return palindromcount
print(zad4(genez))


