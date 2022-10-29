# sito_1 czas dzialania 43,35s
# sito_2 czas dzialania 26,74s (poprawia z pierw)
# sito_3 czas dzialania ???s (poprawia z pierw i kwadratem)

# O(n * log(log(n)))

# n = 30
# n + n/2 + n/3 + n/5 + ... + n/p dla wszystkich p pierw. <= pierw(n)
# n ( 1 + 1/2 + 1/3 + 1/5 + ... + 1/p dla p - pierw. <= pierw(n) )
# ~ n * log(log( n ))
# https://en.wikipedia.org/wiki/Meissel%E2%80%93Mertens_constant


def sito(n):
  # lista od 0 do n wypelniona falszem
  # falsz = nie zostala wykreslona
  s = [False for _ in range(n+1)]
  s[0] = s[1] = True # wykreslam 0 i 1, bo nie sa pierwsze
  for i in range(2, int(n**0.5)+1): # od 2 do pierw(n) rób:
    if s[i] == False: # jesli nie zostala wykreslona to:
      # wykreslamy jej wszystkie wielokrotnosci
      # (wystarczy nam zaczac od i*i
      # bo liczby postaci i * k dla k < i juz zostaly wykreslone)
      for j in range(i*i, n+1, i): # od i*i do n co i rób:
        s[j] = True # skresl j
  return s # zwroc sito

def ile_pierwszych(n):
  s = sito(n)
  wynik = 0
  for i in range(1, n):
    if s[i] == False: wynik += 1
  return wynik

print(ile_pierwszych(100000000))