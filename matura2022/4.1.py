def read_files():
    with open("rrr.txt", "r") as f1:
        file1=[int(x.strip()) for x in f1.readlines()]
    with open("przyklad.txt","r") as f2:
        file2=[int(y.strip()) for y in f2.readlines()]
    return (file1,file2)
numbers,example=read_files()


def zad41(numlist):
    firstnunm=2137
    for num in numlist:
        if str(num)[0]==str(num)[-1]:
            firstnunm=num
            break
    numberscount=0
    for num in numlist:
        if str(num)[0]==str(num)[-1]:
            numberscount+=1


    return (firstnunm,numberscount)
print(zad41(numbers))
