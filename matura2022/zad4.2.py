def read_files():
    with open("rrr.txt", "r") as f1:
        file1=[int(x.strip()) for x in f1.readlines()]
    with open("przyklad.txt","r") as f2:
        file2=[int(y.strip()) for y in f2.readlines()]
    return (file1,file2)
liczby,przyklad=read_files()
def divide_bumber_to_prime_numbers(num):
    divided_numbers=[]

    testetnumber=num
    if num<=3:
        return "nie da się"
    i=2
    while i<=int(testetnumber**0.5)+1:
        while num%i==0:
            num/=i
            divided_numbers.append(i)
        i+=1
    return divided_numbers
def test():
    assert len(divide_bumber_to_prime_numbers(4))==2
    assert len(divide_bumber_to_prime_numbers(7))==0
    assert len(divide_bumber_to_prime_numbers(8))==3
    assert len(divide_bumber_to_prime_numbers(12))==3
    #print("TESTY OK")
test()

def zad_first_line(file):
    count=-99999999999999999999
    resultnumber=[]
    for number in file:
        if len(divide_bumber_to_prime_numbers(number))>count:
            count=len(divide_bumber_to_prime_numbers(number))
            resultnumber=[]
        if len(divide_bumber_to_prime_numbers(number))==count:
            resultnumber.append(number)

    return resultnumber,count
def zad_second_line(file):
    count = -99999999999999999999
    resultnumber = -9099999999999999999999999999
    for number in file:
        if len(set(divide_bumber_to_prime_numbers(number))) > count:
            count = len(set(divide_bumber_to_prime_numbers(number)))
            resultnumber = number

    return resultnumber, count
#n1,n2=zad_first_line(przyklad)
#n3,n4=zad_second_line(przyklad)
n1,n2=zad_first_line(liczby)
n3,n4=zad_second_line(liczby)
print(n1,n2,n3,n4)