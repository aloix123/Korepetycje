def readData():
    with open("festyn.txt","r") as festyn:
        x=[list(map(int,x.split())) for x in festyn.readlines()]
        resultlist=[]
        partlist=[]
        shields=[]
        points=[]
        firindex=1

        while firindex<len(x)-1:
            if len(x[firindex])==2:

                shields.append(x[firindex])
                if len(x[firindex+1])==1:
                    partlist.append(shields)
                    shields = []


            if len(x[firindex])==1:
                points.append(x[firindex])
                if  firindex==len(x)-2:

                    points.append(x[-1])

                    partlist.append(points[1:])
                    points=[]
                elif len(x[firindex+1])==2 :
                    partlist.append(points[1:-1])
                    points=[]

            if len(partlist)==2:
                resultlist.append(partlist)
                partlist=[]
            firindex+=1

        return resultlist


data=readData()

def zad1(data):

    for line in data:
        result=0
        secSumList=[sum(x) for x in line[0]]

        for shoot in secSumList:
            k = 0
            for x in line[1]:

                if x[0]>=line[0][k][0] and x[0]<=shoot:
                    pass


def zad2(data):
    pass
print(zad1(data))

