# Lista zadan pojawiajacych sie na maturach autorstwa Bartosza Bednarczyka
# Temat 1: Algorytmy operujace na cyfrach

# Uwaga: Twoje algorytmy mogą używać wyłącznie zmiennych przechowujących liczby
# całkowite oraz może operować wyłącznie na liczbach całkowitych.
# W zapisie algorytmów możesz korzystać tylko z instrukcji sterujących,
# operatorów arytmetycznych: dodawania, odejmowania, mnożenia, dzielenia,
# dzielenia całkowitego i reszty z dzielenia; operatorów logicznych,
# porównań i instrukcji przypisywania lub samodzielnie
# napisanych funkcji i procedur wykorzystujących powyższe operacje.
# Zabronione jest używanie funkcji wbudowanych dostępnych w Pythonie.
# Nie wolno w szczególności korzystać z żadnych funkcji zamiany
# z typu znakowego lub napisowego na liczbowy i odwrotnie.

# Zad 1
# Input: Nieujemna liczba całkowita n
# Output: suma cyfr liczby n
def suma_cyfr(n):

    result=0
    while n!=0:

        result+=n%10
        n = n // 10
        print(n)
    return result






assert suma_cyfr(0) == 0
assert suma_cyfr(1) == 1
assert suma_cyfr(12) == (1 + 2)
assert suma_cyfr(123) == (1 + 2 + 3)


# Zad 2
# Input: Nieujemna liczba całkowita n
# Output: długość liczby n w zapisie dziesiętnym
def liczba_cyfr(n):

    i=10
    x=1
    while i<n:
        i*=10
        x+=1
    return x


assert liczba_cyfr(0) == 1
assert liczba_cyfr(7) == 1
assert liczba_cyfr(12) == 2
assert liczba_cyfr(123) == 3
assert liczba_cyfr(1222) == 4


# Zad 3
# Input: Nieujemna liczba całkowita n
# Output: Liczba różnych cyfr wystepujacych w zapisie liczby n.

def liczba_roznych_cyfr(n):
    numebers=[]
    numbercount=liczba_cyfr(n)
    while numbercount!=0:
        numebers.append(n//10**(numbercount-1))
        n-=10**(numbercount-1)
        numbercount-=1
    #sortowanie

assert liczba_roznych_cyfr(111111) == 1
assert liczba_roznych_cyfr(123) == 3
assert liczba_roznych_cyfr(12332212) == 3
assert liczba_roznych_cyfr(10234) == 5
assert liczba_roznych_cyfr(101) == 2
assert liczba_roznych_cyfr(7) == 1


# Zad 4
# Input: Nieujemna liczba całkowita n
# Output: True jesli ciag cyfr liczby n jest scisle rosnacy i False w.p.p.

def czy_cyfry_stanowia_ciag_rosnacy(n):
    pass


assert czy_cyfry_stanowia_ciag_rosnacy(7) == True
assert czy_cyfry_stanowia_ciag_rosnacy(123) == True  # tak, bo 1 < 2 < 3
assert czy_cyfry_stanowia_ciag_rosnacy(147) == True
assert czy_cyfry_stanowia_ciag_rosnacy(24689) == True
assert czy_cyfry_stanowia_ciag_rosnacy(79) == True
assert czy_cyfry_stanowia_ciag_rosnacy(321) == False
assert czy_cyfry_stanowia_ciag_rosnacy(122) == False  # nie bo 2 nie jest < 2
assert czy_cyfry_stanowia_ciag_rosnacy(1223) == False


# Pomocnicze pod-zadanie
# Input: Nieujemna liczba całkowita n
# Output: n! (silnia z n)
def silnia(n):
    pass


assert silnia(0) == 1
assert silnia(1) == 1
assert silnia(2) == 1 * 2
assert silnia(3) == 1 * 2 * 3
assert silnia(4) == 1 * 2 * 3 * 4
assert silnia(5) == 1 * 2 * 3 * 4 * 5


# Zad 5
# Input: Nieujemna liczba całkowita n
# Output: True jeżeli liczba jest równa silnii swoich cyfr
def czy_rowny_silnii_swoich_cyfr(n):
    pass


assert czy_rowny_silnii_swoich_cyfr(343) == False  # (3!+4!+3! = 36 =/= 343)
assert czy_rowny_silnii_swoich_cyfr(145) == True  # (1!+4!+5! = 1+24+120 = 145).


# Zad 6
# Niech s(n) oznacza sumę cyfr liczby n.
# Dla danej liczby n tworzymy ciąg zaczynający się od n,
# którego każdy element jest sumą cyfr poprzedniego elementu.
# Znaczkami: a1 = s(n), a2 = s(a1), a3 = s(a2), itd.
# Ciąg kończy się, gdy jego wyraz jest liczbą jednocyfrową.
# Tę liczbę nazywamy wagą liczby n.

# Input: Nieujemna liczba całkowita n
# Output: waga n

def waga(n):
    pass


assert waga(1109) == 2
assert waga(31699) == 1
assert waga(8) == 8


# Zad 7
# Liczby x i y nazwiemy cyfropodobnymi,
# jeżeli do ich zapisania użyliśmy dokładnie tych samych
# cyfr dziesiętnych (by może inną liczbę razy).

# Input: Nieujemne liczby całkowite x,y
# Output: True jesli x i y sa cyfropodobne i False w.p.p.

def czy_cyfropodobne(x, y):
    pass


assert czy_cyfropodobne(111, 12) == False
assert czy_cyfropodobne(121, 12) == True
assert czy_cyfropodobne(123, 321) == True


# Zad 8
# Powiemy, że dwie liczby naturalne a i b są anagramami cyfrowymi,
# jeśli liczbę a (symetrycznie b) można zapisać dziesiętnie za pomocą
# cyfr występujących w zapisie dziesiętnym liczby b (symetrycznie a),
# używając każdej cyfry dokładnie tyle razy, ile razy występuje w zapisie b
# (symetrycznie w zapisie a). Uwaga: przyjmujemy, że w zapisie dziesiętnym żadnej
# liczby nie ma nieznaczących 0, co oznacza, że 0 występuje na najbardziej
# znaczącej pozycji tylko w zapisie liczby zero.

# Input: Nieujemne liczby całkowite a,b
# Output: True jesli x i y sa anagramami cyfrowymi i False w.p.p.

def czy_anagramamy_cyfrowe(a, b):
    pass


assert czy_anagramamy_cyfrowe(232, 322) == True
assert czy_anagramamy_cyfrowe(232, 322) == True
assert czy_anagramamy_cyfrowe(322, 223) == True
assert czy_anagramamy_cyfrowe(223, 322) == True
assert czy_anagramamy_cyfrowe(111, 11) == False
assert czy_anagramamy_cyfrowe(123, 3212) == False
assert czy_anagramamy_cyfrowe(123, 3217) == False


# Zad 9
# Input: Nieujemna liczba całkowita n
# Output: Wartość 2**n modulo 10
# Uwaga! Docelowa złożonoć twojego rozwiązania to O(1)

def ostatnia_cyfra_potegi_2(n):
    pass


for i in range(0, 10):
    assert ostatnia_cyfra_potegi_2(i) == (2 ** i % 10)


# Zad 10
# Niech n będzie nieujemną liczbą całkowitą, której najbardziej znacząca
# cyfra w zapisie dziesiętnym jest większa od 0 i mniejsza od 9.
# Cyfrowym dopełnieniem liczby n nazywamy liczbę całkowitą d, której zapis
# dziesiętny otrzymujemy z zapisu dziesiętnego liczby n przez zamianę
# każdej cyfry tego zapisu na cyfrę, która jest jej uzupełnieniem do 9.
# O liczbie n wiadomo, że jej najbardziej znacząca cyfra
# jest większa od 0 i mniejsza od 9 (nie musisz tego sprawdzać).
# Input: Nieujemna liczba całkowita n
# Output: Cyfrowe dopełnienie n

def cyfrowe_dopelnienie(n):
    return n
    pass


assert cyfrowe_dopelnienie(2021) ==7978
assert cyfrowe_dopelnienie(876) == 123
assert cyfrowe_dopelnienie(123) == 876


# Zad 11
# Liczba całkowita złożona z n cyfr jest liczbą Armstronga (narcystyczną),
# jeżeli jest sumą swoich cyfr podniesionych do potęgi n.
# Na przykład: 153 = 1^3+5^3+3^3 = 1+125+27.
# Input: Nieujemna liczba całkowita n
# Output: True jezeli n jest liczba Armstronga i False w.p.p.

def czy_liczba_Armstronga(n):
    pass


assert czy_liczba_Armstronga(153) == True
assert czy_liczba_Armstronga(370) == True
assert czy_liczba_Armstronga(371) == True
assert czy_liczba_Armstronga(407) == True
assert czy_liczba_Armstronga(1634) == True
assert czy_liczba_Armstronga(8208) == True
assert czy_liczba_Armstronga(9474) == True
assert czy_liczba_Armstronga(123) == False
assert czy_liczba_Armstronga(12) == False
assert czy_liczba_Armstronga(0) == False



