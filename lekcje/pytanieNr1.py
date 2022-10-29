#Jak rozbić licizbę na czynniki pierwsze? Jak poliiczyć jej liiczbę czynnikków pierszychh?
#proste

def divide_bumber_to_prime_numbers(num):
    divided_numbers=[]
    counter=0
    testetnumber=num
    if num<=3:
        return "nie da się"
    i=2
    while i<=int(testetnumber**0.5)+1:
        while num%i==0:
            num/=i
            counter+=1
            divided_numbers.append(i)
        i+=1
    return (divided_numbers,counter)
print(divide_bumber_to_prime_numbers(12))