# O(max(L) + |L|)
def tablica_zliczen(L):
  m = max(L) # O(|L|)
  W = [0 for _ in range(m+1)] # O(m)
  for x in L: # O(|L|)
    W[x] += 1
  return W

# Ciag n liczb nazywamy n-PERMUTACJĄ,
# wtedy kiedy każda z liczb od 1 do n
# występuje w tym ciągu dokładnie raz.
# np. 1 2 3 jest 3-permutacja
# np. 3 1 2 jest 3-permutacja
# np. 1 2 3 3 nie jest 4-permutacja
# np. 1 2 1 3 nie jest 4-permutacja
# np. -1 2 874621786421786412 nie jest 3-permutacja

def czy_n_permutacja(L, n):
  
  if not (min(L)==1 and max(L)==n and len(L)==n):
    return  "NIE"
  w=tablica_zliczen(L)[1:]
  for number in w:
    if number!=1:
      return "NIE"



  return "TAK"
n=int(input())
table=list(map(int,input().split()))
print(czy_n_permutacja(table,n))