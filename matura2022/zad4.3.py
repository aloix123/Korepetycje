def read_files():
    with open("rrr.txt", "r") as f1:
        file1=[int(x.strip()) for x in f1.readlines()]
    with open("przyklad.txt","r") as f2:
        file2=[int(y.strip()) for y in f2.readlines()]
    return (file1,file2)
numbers,example=read_files()

def zad43(numlits):
    resultlist=[]
    resultfifelist=[]
    for index in range(0,len(numlits)):
        firstnum=numlits[index]

        for secindex in range(0,len(numlits)):
            secnum=numlits[secindex]

            if secnum%firstnum==0 and secindex!=index:
                for thirdindex in range(0,len(numlits)):
                    thirdnum=numlits[thirdindex]
                    if thirdnum%secnum==0 and thirdindex!=secindex:

                        resultlist.append([firstnum,secnum,thirdnum])
    trojki = open("trojki.txt", "w")
    for number in resultlist:

        trojki.write(f"{number[0]} {number[1]} {number[2]}")
        trojki.write("\n")
    trojki.close()

    for index in range(0, len(numlits)):
        firstnum = numlits[index]

        for secindex in range(0, len(numlits)):
            secnum = numlits[secindex]

            if secnum % firstnum == 0 and secindex != index:
                for thirdindex in range(0, len(numlits)):
                    thirdnum = numlits[thirdindex]
                    if thirdnum % secnum == 0 and thirdindex != secindex:
                        for fourindex in range(len(numlits)):
                            four=numlits[fourindex]
                            if four % thirdnum == 0 and thirdindex != fourindex:
                                for fifthindex in range(len(numlits)):
                                    fifve= numlits[fifthindex]
                                    if fifve% four == 0 and fifthindex != fourindex:
                                        resultfifelist.append([firstnum, secnum, thirdnum,four,fifve])
    return f"{len(resultlist)} {len(resultfifelist)}"

#only God and i can understand whot is going on in this code

print(zad43(numbers))
