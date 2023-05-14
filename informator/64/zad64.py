def readData():
    with open("dane_obrazki.txt","r") as pictures:
        x1=[x.strip() for x in pictures.readlines()]
        data=[]
        pomlist=[]

        for i in range(4399):
            if x1[i]=='':
                data.append(pomlist)
                pomlist.clear()

            else:
                pomlist.append(x1[i])
    data.reverse()
    return data

data=readData()
print(len(data))
def zad1(data):
    reverseCount=0
    maxblack=0
    for image in data:
        localblack = 0
        localwhite = 0#NWM jak to zrobić

        for line in range(len(image)-1):

            for pixel in range(len(image)-1):
                if image[line][pixel]=="1":
                    localblack+=1
                else:
                    localwhite+=1
        if localblack>localwhite:
            reverseCount+=1
            maxblack=max(maxblack,localblack)
    return (reverseCount,maxblack)
print(zad1(data))
