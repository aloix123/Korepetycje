def is_prime(n):#kradzione
  if n< 2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True
def is_super_prime(n):
  b=0
  for num in str(n):
    b+=int(num)
  if is_prime(n) and is_prime(int(b)):
    return True
  return False
def is_super_B_prime(n):
  c=str(bin(n))[2:]

  x=0
  for num in c:
    x+=int(num)

  if is_super_prime(n) and is_prime(x):
    return True
  return False
def test():

  assert  is_prime(7)
  assert  is_prime(11)
  assert  is_prime(17)
  assert  is_prime(13)
  assert  is_prime(3)
  assert is_super_prime(3)
  assert is_super_prime(23)
  assert is_super_prime(7)
  assert is_super_prime(11)
  assert is_super_B_prime(11)
  assert is_digit_sum_prime(23)
  assert is_digit_sum_prime(102)
  assert is_digit_sum_prime(21)
  assert is_digit_sum_prime(16)
  assert is_digit_sum_prime(3)
  assert is_digit_sum_prime(2)

  print("TESTY OK")
def wczytajpliki():
  plik1  =open("1.txt","w")
  plik2 = open("2.txt", "w")
  plik3 = open("3.txt", "w")
  return (plik1,plik2,plik3)
def otwórz_2_txt():
  with open('2.txt', 'r') as plik:
    x = [a.strip() for a in plik.readlines()]
  return x
#TODO zadania a b c
def zad_a(firstnum,lastnum,file):
  result=0
  for a in range(firstnum,lastnum):
    if is_super_B_prime(a):
      result+=1
      file.writelines(str(a)+" \n")
  file.close()
  return result

def is_digit_sum_prime(num):
  numbersum=0
  for digit in str(num):
    numbersum+=int(digit)
  return is_prime(numbersum)
def zad_b(firstnum,lastnum):
  count=0
  for a in range(firstnum, lastnum):
    if is_digit_sum_prime(a):
      count+=1
  return count
def zad_c(firstnum,lastnum,file):
  MAX_NUMBER_OF_B_PRIME_NUMS=249
  indexchecker=0

  for number in file:
    if is_digit_sum_prime(number):
      indexchecker+=1
      print(indexchecker)
  if MAX_NUMBER_OF_B_PRIME_NUMS==indexchecker:
    return "tak"
  else:
    return "nie"

t1,t2,t3=wczytajpliki()


print(zad_a(2,1000,t1))
print(zad_a(100,10000,t2))
print(zad_a(1000,100000,t3))
print(zad_b(100,10000))
d2=otwórz_2_txt()
print(zad_c(1000,100000,d2))
test()
#a)
#1 50
#2 249
#1262
#b)2973
#tak są