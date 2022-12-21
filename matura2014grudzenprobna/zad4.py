import math

def zad41():
    r = 5
    T = 12.5
    deltaT = 0.05
    tStart = 3
    x = 1
    y = 0

    while x > y:
        tStart += deltaT
        x =r*math.sin(2*math.pi*tStart/T)
        y = r * math.cos(2 * math.pi * tStart / T)

    return round(tStart,2)
#zad42 tylko exel
def zad43():
    points=[]
    firstpoint=[0,0]
    points.append(firstpoint)
    distance=[]
    r = 5
    T = 10
    deltaT = 0.5
    tStart = 0
    maxt=10
    v=1
    i=1
    while tStart<=maxt:
        r=v*tStart
        x = r * math.sin(2 * math.pi * tStart / T)
        y = r * math.cos(2 * math.pi * tStart / T)
        points.append([x,y])
        calkulatedDistance=math.sqrt((points[i][0]-points[i-1][0])**2+(points[i][1]-points[i-1][1])**2)
        distance.append(calkulatedDistance)
        tStart+=deltaT
        i+=1
    return round(sum(distance),4)



print(zad41())
print(zad43())





