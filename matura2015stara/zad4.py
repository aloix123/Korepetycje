def readData():
    with open("slowa.txt") as words:
        x1=[x for x in words.readlines()]
    return x1
w=readData()

def zad1(w):
    result=0
    for number in w:

        if str(number).count('0')>str(number).count('1'):
            result+=1
    return result
def zad2(words):
    result=0
    x=0
    for word  in words:
        circle = 0

        zero=word.find('1')
        print(zero)
        if zero==len(word)+1:
            circle+=1
        for digit in range(zero,len(word)):
            if word[digit]=='0':
                circle+=1
        if circle==0:
            result+=1

    return result



print(zad1(w))
print(zad2(w))