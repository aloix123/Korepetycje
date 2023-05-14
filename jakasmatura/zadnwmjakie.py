def readData():
    with open("liczby.txt","r") as nums:
        x1=[list(map(int,x.split())) for x in nums.readlines()]
    return x1
data=readData()
def zad1(numbers):
    sum1=0
    sum2=0
    for line in numbers:
        for num in line:
            if "0" not in str(num):
                if num>0:
                    sum1+=num
                else:
                    sum2+=num
    return f"suma więkrzych od 0 {sum1} , sumalicz mniejszych od 0 {sum2}"
def zad2(numbers):
    raisingSeriesCount=0
    loweringSeriesCount=0
    for index  in range(len(numbers)-2):
        if numbers[index][0]<numbers[index+1][0] and numbers[index+1][0]<numbers[index+2][0]:

            raisingSeriesCount+=1
    for index  in range(len(numbers)-2):
        if numbers[index][1] > numbers[index + 1][1] and numbers[index + 1][1] > numbers[index + 2][1]:

            loweringSeriesCount+=1
    return f"liczba ciągów rosnocych {raisingSeriesCount} i malejących {loweringSeriesCount}"
def zad3(numbers):
    i=0
    l=len(numbers)
    while i<l-1:
        k=i+1
        while k<l-1:
            if numbers[i][1]==numbers[k][0]:
                p=[numbers[i][1],numbers[k][0]]
                numbers.remove(numbers[i])
                numbers.remove(numbers[k])
                numbers.append(p)
                l=len(numbers)
            k+=1
        i+=1
    return numbers

print(zad1(data))
print(zad2(data))
print(zad3(data))