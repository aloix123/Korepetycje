def readData():
    with open("galerie.txt") as galery:
        x1=[list(x.split()) for x in galery.readlines()]
    with open("galerie_przyklad.txt") as example:
        x2=[list(x.split()) for x in example.readlines()]
    return (x1,x2)
galery,example=readData()

def zad1(data):
    countryDicct={}
    for line in data:
        countryDicct[line[0]]=0
    for line in data:
        countryDicct[line[0]]+=1
    for index in countryDicct:
        print(f"{index} {countryDicct[index]}")
    return 0
def zad2(data):
    localcount=[]
    citiesTab=[]
    sphereTab=[]
    for line in data:
        citiesTab.append(line[1])
        localamount=len(line[2:])/2
        for indexd in range(2,len(line),2):
            if int(line[indexd])==0 and int(line[indexd+1])==0:
                localamount-=1
        localcount.append(localamount)
        sphere=0
        for index in range(2,len(line),2):
            sphere+=int(line[index])*int(line[index+1])
        sphereTab.append(sphere)
    for resultindex in range(len(data)):
        print(f"{citiesTab[resultindex]} {sphereTab[resultindex]} {localcount[resultindex]}  ")
    minsphere=min(sphereTab)
    maxsphere=max(sphereTab)
    indexmax=0
    indexmin=0
    for y in range(len(sphereTab)):
        if sphereTab[y]==maxsphere:
            indexmax=y
        if sphereTab[y]==minsphere:
            indexmin=y
    print(f"najmniejsza pow {citiesTab[indexmin]} {minsphere}")
    print(f"najwiękrza pow {citiesTab[indexmax]} {maxsphere}")

def zad3(data):
    maxgallery=0
    mingallery=99999999999999
    mincity=''
    maxcity=""

    for line in data:

        samegalleryCount=0
        sphere = []
        for index in range(2,len(line),2):
            sphere.append(int(line[index])*int(line[index+1]))
        samegalleryCount=len(set(sphere))-1
        if samegalleryCount>maxgallery:
            maxgallery=samegalleryCount
            maxcity=line[1]
        if samegalleryCount<mingallery:
            mingallery=samegalleryCount
            mincity=line[1]
    print(f"najmniej tych samych lokali {mincity} {mingallery}")
    print(f"najwięcej tych samych lokali {maxcity} {maxgallery}")

def test():
    #zad1(example)
    pass

test()
#zad1(galery)
#zad2(galery)
zad3(galery)