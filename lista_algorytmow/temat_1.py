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
    while i<=n:
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
    lengh = liczba_cyfr(n)

    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    i0=0
    x = liczba_cyfr(n) - 1
    for i in range(lengh):

        cyfra = n // 10 ** (x)


        if cyfra==1:
            i1=1
        if cyfra==0:
            i0=1
        elif cyfra==2:
            i2=1
        elif cyfra==3:
            i3=1
        elif cyfra==4:
            i4=1
        elif cyfra==5:
            i5=1
        elif cyfra==6:
            i6=1
        elif cyfra==7:
            i7=1
        elif cyfra==8:
            i8=1
        elif cyfra==9:
            i9=1
        n = n - 10 ** (x) * cyfra
        x -= 1

    result=i1+i2+i3+i4+i5+i6+i7+i8+i9+i0
    return result

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
    index = -9999999999999999999999999999999999999999
    lengh = liczba_cyfr(n)
    x = liczba_cyfr(n) - 1
    for i in range(lengh):
        cyfra = n // 10 ** (x)
        n = n - 10 ** (x) * cyfra
        if index < cyfra:
            index = cyfra
        else:
            return False
        x -= 1
    return True



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
    if n<=1:
        return 1
    return silnia(n-1)*n




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
    firstnumber=n
    lengh = liczba_cyfr(n)
    x = liczba_cyfr(n) - 1
    result=0
    for i in range(lengh):
        cyfra = n // 10 ** (x)

        result+=silnia(cyfra)
        n = n - 10 ** (x) * cyfra
        x-=1

    return firstnumber==result


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


    result = n
    lengh = liczba_cyfr(result)
    x = liczba_cyfr(result) - 1
    y=liczba_cyfr(result)
    while y>1:
        index=0

        for i in range(lengh):
            cyfra = result // 10 ** (x)
            index+=cyfra
            result=result - 10 ** (x) * cyfra
            x -= 1

        result = index
        x = liczba_cyfr(result) - 1

        y = liczba_cyfr(result)

        lengh = liczba_cyfr(result)


    return result






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
    lenghx = liczba_cyfr(x)
    lenghy = liczba_cyfr(y)
    i1 = 0;y1=0
    i2 = 0;y2=0
    i3 = 0;y3=0
    i4 = 0;y4=0
    i5 = 0;y5=0
    i6 = 0;y6=0
    i7 = 0;y7=0
    i8 = 0;y8=0
    i9 = 0;y9=0
    i0 = 0;y0=0

    index = liczba_cyfr(x) - 1
    for i in range(lenghx):
        cyfra = x // 10 ** (index)
        if cyfra == 1:
            i1 = 1
        if cyfra == 0:
            i0 = 1
        elif cyfra == 2:
            i2 = 1
        elif cyfra == 3:
            i3 = 1
        elif cyfra == 4:
            i4 = 1
        elif cyfra == 5:
            i5 = 1
        elif cyfra == 6:
            i6 = 1
        elif cyfra == 7:
            i7 = 1
        elif cyfra == 8:
            i8 = 1
        elif cyfra == 9:
            i9 = 1
        x = x - 10 ** (index) * cyfra
        index -= 1
    indey = liczba_cyfr(y) - 1
    for i in range(lenghy):
        cyfra = y // 10 ** (indey)
        if cyfra == 1:
            y1 = 1
        if cyfra == 0:
            y0 = 1
        elif cyfra == 2:
            y2 = 1
        elif cyfra == 3:
            y3 = 1
        elif cyfra == 4:
            y4 = 1
        elif cyfra == 5:
            y5 = 1
        elif cyfra == 6:
            y6 = 1
        elif cyfra == 7:
            y7 = 1
        elif cyfra == 8:
            y8 = 1
        elif cyfra == 9:
            y9 = 1
        y = y - 10 ** (indey) * cyfra
        indey -= 1
    resultx = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i0
    resulty=y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y0

    return resulty==resultx


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
    x=a
    y=b
    lenghx = liczba_cyfr(x)
    lenghy = liczba_cyfr(y)
    i1 = 0;
    y1 = 0
    i2 = 0;
    y2 = 0
    i3 = 0;
    y3 = 0
    i4 = 0;
    y4 = 0
    i5 = 0;
    y5 = 0
    i6 = 0;
    y6 = 0
    i7 = 0;
    y7 = 0
    i8 = 0;
    y8 = 0
    i9 = 0;
    y9 = 0
    i0 = 0;
    y0 = 0

    index = liczba_cyfr(x) - 1
    for i in range(lenghx):
        cyfra = x // 10 ** (index)
        if cyfra == 1:
            i1 = 1
        if cyfra == 0:
            i0 = 1
        elif cyfra == 2:
            i2 = 1
        elif cyfra == 3:
            i3 = 1
        elif cyfra == 4:
            i4 = 1
        elif cyfra == 5:
            i5 = 1
        elif cyfra == 6:
            i6 = 1
        elif cyfra == 7:
            i7 = 1
        elif cyfra == 8:
            i8 = 1
        elif cyfra == 9:
            i9 = 1
        x = x - 10 ** (index) * cyfra
        index -= 1
    indey = liczba_cyfr(y) - 1
    for i in range(lenghy):
        cyfra = y // 10 ** (indey)
        if cyfra == 1:
            y1 = 1
        if cyfra == 0:
            y0 = 1
        elif cyfra == 2:
            y2 = 1
        elif cyfra == 3:
            y3 = 1
        elif cyfra == 4:
            y4 = 1
        elif cyfra == 5:
            y5 = 1
        elif cyfra == 6:
            y6 = 1
        elif cyfra == 7:
            y7 = 1
        elif cyfra == 8:
            y8 = 1
        elif cyfra == 9:
            y9 = 1
        y = y - 10 ** (indey) * cyfra
        indey -= 1
    return (i1==y1 and i2==y2 and i3==y3 and i4==y4 and i5==y5 and i6==y6 and i7==y7 and i8==y8 and i9==y9 and i1==y0)


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
    if n==0:
        return 1
    n=n%4
    if n==0:
        return 6
    elif n==1:
        return 2
    elif n==2:
        return 4
    elif n==3:
        return 8



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
    lengh=liczba_cyfr(n)
    index = liczba_cyfr(n) - 1
    result=0
    for i in range(lengh):
        cyfra = n // 10 ** (index)
        n= n - 10 ** (index) * cyfra
        dop=9-cyfra

        result+=10**(index) * dop
        index -= 1

    return result

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
    oldn=n
    h=liczba_cyfr(n)
    lengh = liczba_cyfr(n)
    index = liczba_cyfr(n) - 1
    result = 0
    if n==0:
        return False
    for i in range(lengh):
        cyfra = n // 10 ** (index)

        result+=cyfra**h
        n = n - 10 ** (index) * cyfra


        index -= 1
    return result==oldn




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



