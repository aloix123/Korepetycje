# Lista zadan pojawiajacych sie na maturach autorstwa Bartosza Bednarczyka
# Temat 2: Algorytmy operujace na tekstach

# Uwaga: Twoje algorytmy mogą używać wyłącznie zmiennych przechowujących liczby
# całkowite oraz napisów.
# W zapisie algorytmów możesz korzystać tylko z instrukcji sterujących,
# operatorów arytmetycznych: dodawania, odejmowania, mnożenia, dzielenia,
# dzielenia całkowitego i reszty z dzielenia, kontkatenacji napisów;
# operatorów logicznych, porównań i instrukcji przypisywania lub samodzielnie
# napisanych funkcji i procedur wykorzystujących powyższe operacje.
# Zabronione jest używanie funkcji wbudowanych dostępnych w Pythonie
# oprócz funkcji len, chr, ord.
# Nie wolno w szczególności korzystać z żadnych funkcji zamiany
# z typu znakowego lub napisowego na liczbowy i odwrotnie.

# Zad 1
# Palindrom to słowo, które czytanie od prawej do lewej i od lewej do prawej jest takie samo.
# Input: Słowo s
# Output: True jeżeli s jest palindromem i False w.p.p

def czy_palindrom(s):
    lengh=len(s)
    if lengh%2!=0:
      lengh-=1
    lengh//=2
    index=len(s)-1
    for i in range(lengh+1):
        if s[i]!=s[index-i]:
          return False
    return True



assert czy_palindrom("kajak") == True
assert czy_palindrom("a") == True
assert czy_palindrom("aba") == True
assert czy_palindrom("ab") == False
assert czy_palindrom("abaa") == False

# Zad 2
# Słowa a i b są anagramami, jeżeli używają dokładnie tych samych liter dokładnie tyle samo razy.
# Przykład: "iamlordvoldemort" i "tommarvoloriddle"
# Input: Słowa a i b.
# Output: True jeżeli a i b są anagramami.
# UWAGA: Docelowa zloznosc twojego rozwiazania to O(|a| + |b|)

def czy_anagramy(a,b):
    ile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in a: ile[ord(c) - ord('a')] += 1
    for c in b: ile[ord(c) - ord('a')] -= 1
    for i in range(0, 26):
        if ile[i] != 0: return False
    return True




assert czy_anagramy("iamlordvoldemort", "tommarvoloriddle") == True
assert czy_anagramy("abc", "cba") == True
assert czy_anagramy("aaa", "a") == False
assert czy_anagramy("abcb", "cba") == False
assert czy_anagramy("xyz", "abc") == False

# Zad 3
# Input: Słowo s.
# Output: Litera, która występuje najczęściej i liczbę jej wystąpień.
# Jeżeli jest wiele takich liter, to odpowiedzią powinna
# być litera najwcześniejsza w alfabecie, która występuje najczęściej.
# UWAGA: Docelowa zloznosc twojego rozwiazania to O(|s|)

def najczestsza_litera_oraz_liczba_jej_wystapien(s):
    ile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in s: ile[ord(c) - ord('a')] += 1
    indexlitery=0
    ilosclitery=0
    for i in range(len(ile)):
        if ile[i]>ilosclitery:
            ilosclitery=ile[i]
            indexlitery=i

    return (chr(indexlitery+97),ilosclitery)

assert najczestsza_litera_oraz_liczba_jej_wystapien("abca") == ('a', 2)
assert najczestsza_litera_oraz_liczba_jej_wystapien("abcab") == ('a', 2)
assert najczestsza_litera_oraz_liczba_jej_wystapien("xyz") == ('x', 1)
assert najczestsza_litera_oraz_liczba_jej_wystapien("abcdefabcb") == ('b', 3)
assert najczestsza_litera_oraz_liczba_jej_wystapien("l") == ('l', 1)
assert najczestsza_litera_oraz_liczba_jej_wystapien("xy") == ('x', 1)


# Zad 4
# Input: Słowo s.
# Output: Liczbę różnych liter występujących w s.
# UWAGA: Docelowa zloznosc twojego rozwiazania to O(|s|)
def liczba_roznych_liter(s):
    ile = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in s: ile[ord(c) - ord('a')] += 1
    ileroznychlicb=0
    for i in range(len(ile)):
        if ile[i] !=0:
            ileroznychlicb+=1
    return ileroznychlicb


pass

assert liczba_roznych_liter("abc") == 3
assert liczba_roznych_liter("abcabc") == 3
assert liczba_roznych_liter("aaaaaaaaaa") == 1
assert liczba_roznych_liter("abbbbaaab") == 2
assert liczba_roznych_liter("qwertyuioplkjhgfdsazxcvbnm") == 26


# Zad 5
# Input: Napis złożony z dokładnie 11 cyfr.
# Output: True jeżeli podany napis to to poprawny numer pesel i False w.p.p.
# Algorytm sprawdzania poprawności peselu jest opisany w zad 5 pod adresem
# https://arkusze.pl/maturalne/informatyka-2010-maj-matura-rozszerzona-2.pdf
def czy_poprawny_pesel(s):
    wynik=int(s[0])*1+int(s[1])*3+int(s[2])*7+int(s[3])*9+int(s[4])*1+int(s[5])*3+int(s[6])*7+int(s[7])*9+int(s[8])*1+int(s[9])*3
    resztazwynik=wynik%10
    if resztazwynik==0 and int(s[10])==0:
        return True
    else:
        resztazwynik=10-resztazwynik
        if resztazwynik==int(s[10]):
            return True
    return False


assert czy_poprawny_pesel("75121968629") == True
assert czy_poprawny_pesel("53082806059") == True
assert czy_poprawny_pesel("67103111042") == True
assert czy_poprawny_pesel("74040249598") == True
assert czy_poprawny_pesel("54043010088") == False
assert czy_poprawny_pesel("60061144469") == False
assert czy_poprawny_pesel("77072919805") == False
assert czy_poprawny_pesel("77120835871") == False
assert czy_poprawny_pesel("83041812338") == False
assert czy_poprawny_pesel("89081421445") == False
assert czy_poprawny_pesel("91032272651") == False
assert czy_poprawny_pesel("92022716243") == False

# Zad 6
# Input: Napisy a i b.
# Output: True jeżeli a jest prefiksem b.
def czy_prefiks(a, b):
    if(a==""):
        return True


    for i in range(len(a)):

        if a[i]!=b[i]:
            return False

    return True



assert czy_prefiks("", "abcdefabcb") == True
assert czy_prefiks("a", "abcdefabcb") == True
assert czy_prefiks("ab", "abcdefabcb") == True
assert czy_prefiks("abc", "abcdefabcb") == True
assert czy_prefiks("abcd", "abcdefabcb") == True
assert czy_prefiks("abcde", "abcdefabcb") == True
assert czy_prefiks("abcdef", "abcdefabcb") == True
assert czy_prefiks("abcdefa", "abcdefabcb") == True
assert czy_prefiks("abcdefab", "abcdefabcb") == True
assert czy_prefiks("abcdefabc", "abcdefabcb") == True
assert czy_prefiks("abcdefabcb", "abcdefabcb") == True
assert czy_prefiks("cd", "abcdefabcb") == False
assert czy_prefiks("fab", "abcdefabcb") == False
assert czy_prefiks("bcb", "abcdefabcb") == False
assert czy_prefiks("bc", "abcdefabcb") == False
assert czy_prefiks("abcdefabcb", "bc") == False


# Zad 7
# Input: Napisy a i b.
# Output: True jeżeli a jest sufiksem b.
def czy_sufiks(a, b):
    if (a == ""):
        return True

    for i in range(-1,-len(a)-1,-1):

        if a[i] != b[i]:
            return False

    return True


assert czy_sufiks("abcdefabcb", "abcdefabcb") == True
assert czy_sufiks("bcdefabcb", "abcdefabcb") == True
assert czy_sufiks("cdefabcb", "abcdefabcb") == True
assert czy_sufiks("defabcb", "abcdefabcb") == True
assert czy_sufiks("efabcb", "abcdefabcb") == True
assert czy_sufiks("fabcb", "abcdefabcb") == True
assert czy_sufiks("abcb", "abcdefabcb") == True
assert czy_sufiks("bcb", "abcdefabcb") == True
assert czy_sufiks("cb", "abcdefabcb") == True
assert czy_sufiks("b", "abcdefabcb") == True
assert czy_sufiks("", "abcdefabcb") == True
assert czy_sufiks("ab", "abcdefabcb") == False
assert czy_sufiks("fab", "abcdefabcb") == False
assert czy_sufiks("acb", "abcdefabcb") == False
assert czy_sufiks("bc", "abcdefabcb") == False

# Zad 8
# Input: Napisy a i b.
# Output: True jeżeli słowo a jest zawarte wewnątrz b (a jest infixem b).
# Uwaga: Mówimy też, że a jest podsłowem b.
def czy_wewnatrz(a, b):
  startlitera=0
  i=0
  while i<len(b):
      if a[0]==b[i]:
          startlitera=i
          i+=len(b)
      i+=1

  index=0

  for x in range(len(a)):

      if a[index]!=b[startlitera+x]:
          return False
      index+=1

  return True


assert czy_wewnatrz("abcdefabcb", "abcdefabcb") == True
assert czy_wewnatrz("abcdefabcb", "abcdefabcb") == True
assert czy_wewnatrz("abcdefabcb", "abcdefabcb") == True
assert czy_wewnatrz("defa", "abcdefabcb") == True
assert czy_wewnatrz("defab", "abcdefabcb") == True
assert czy_wewnatrz("abcd", "abcdefabcb") == True
assert czy_wewnatrz("abdeabb", "abcdefabcb") == False

# Zad 9
# Input: Napisy a i b.
# Output: True jeżeli słowo a jest podciagiem b.
# UWAGA: Słowo a jest podciągiem słowa b, jeśli a może
# powstać z b przez usunięcie niektórych elementów ciągu b
# (w szczególnych przypadkach wszystkich elementów bądź żadnego elementu).
# Themis: CTABLES2

def czy_podciag(a, b):
    aindex=0
    for i in range(len(b)):
        if a[aindex]==b[i]:
            aindex+=1
    if aindex==len(a):
        return True
    else:
        return False


assert czy_podciag("abc", "xyzaxyzbxyzc") == True
assert czy_podciag("abc", "abc") == True
assert czy_podciag("abc", "cba") == False

# Zad 10
# Input: Napis a
# Output: True jeżeli suma kodow ascii slowa a jest liczba pierwsza i False w.p.p.

def czy_slowo_pierwsze(s):
    sumascii=0
    for letter in s:
        sumascii+=ord(letter)

    i=2
    while i<sumascii:

        if sumascii % i ==0:
            return False
        i+=1
    return True


assert czy_slowo_pierwsze("ABB") == True
#assert czy_slowo_pierwsze("AB") == False
assert czy_slowo_pierwsze("A") == False

# Zad 11
# Input: Napis a
# Output: True jeżeli istnieje taka liczba k, ze roznica kodow ascii
# pomiedzy dowolnymi kolejnymi dwoma sasiednimi literami a jest rowna k.

def czy_regularny(a):
    if len(a)==0:
        return "error"

    k=ord(a[0])-ord(a[1])
    start=1
    stringlen=len(a)
    while start<stringlen-1:
        difference=ord(a[start])-ord(a[start+1])

        if difference==k:
            start+=1
        else:
            return False
    return True



assert czy_regularny("aaaaaaaaaaaa") == True
assert czy_regularny("abcdefghi") == True
assert czy_regularny("abcf") == False
assert czy_regularny("aceg") == True

# Zad 12
# Napis nazywać będziemy dwucyklicznym,
#jeśli składa się on wyłącznie z dwóch powtórzeń tego samego napisu.
# Input: Napis a
# Output: True jeżeli a jest dwucykliczny i False w.p.p.

def czy_dwucykliczny(a):
  if len(a)==1:
      return True
  if len(a)==2:
      if a[0]==a[1]:
          return True
      else:
          return False
  middle=0
  if len(a)%2==0:
      middle=len(a)//2
  else:
      return False
  for i in range(len(a)//2):
      if a[i]!=a[middle+i]:
          return False
  return True


assert czy_dwucykliczny("abcabc") == True
assert czy_dwucykliczny("xx") == True
assert czy_dwucykliczny("abab") == True
assert czy_dwucykliczny("abcabcd") == False
assert czy_dwucykliczny("abac") == False
assert czy_dwucykliczny("10001000") == True
assert czy_dwucykliczny("00011000") == False
assert czy_dwucykliczny("10001001") == False

# Zad 13
# Input: Napis a
# Output: True jeżeli kody ascii dowolnych dwóch liter z a róznią się o co najwyżej 10.

def czy_litery_oddalone_o_max_10(a):
  pass

assert czy_litery_oddalone_o_max_10("abcdef") == True
assert czy_litery_oddalone_o_max_10("ax") == False
assert czy_litery_oddalone_o_max_10("abxcdsda") == False
assert czy_litery_oddalone_o_max_10("im") == True

# Zad 14
# Input: Napis a
# Output: True jeżeli napis jest rosnący i False w.p.p.
# Napis nazywamy rosnacym, gdy ciag kodow ascii jego liter jest rosnacy.

def czy_napis_rosnacy(a):
  pass

assert czy_napis_rosnacy("abcdef") == True
assert czy_napis_rosnacy("adef") == True
assert czy_napis_rosnacy("aabcdef") == False
assert czy_napis_rosnacy("abbcdef") == False
assert czy_napis_rosnacy("abccdef") == False
assert czy_napis_rosnacy("abcddef") == False
assert czy_napis_rosnacy("abcdeef") == False
assert czy_napis_rosnacy("abcdeff") == False
assert czy_napis_rosnacy("cba") == False

# Zad 15
# Input: Lista L złożona z napisow.
# Output: Lista L' zawieraja wszystkie napisy wystapujace w L więcej niż raz.
# Lista L' nie powinna zawierać duplikatów i powinna być uporządkowana w.g.
# wystapien słów na liście L.
# W tym zadaniu możesz używać listy i funkcji append.

def usun_duplikaty(L):
  pass

assert usun_duplikaty(["a", "b", "c", "d", "e", "e", "a", "e", "f"]) == ["a", "e"]


# Dodatkowe zadania dla ambitniejszych:
# Zad 4 Luki w ciągu https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-2.pdf
# Zad 27 Dopasowanie z błędem https://www.oke.waw.pl/new/download/files/File/CKE/2016/mat/Matura_Zbi%C3%B3r_zada%C5%84_Informatyka.pdf