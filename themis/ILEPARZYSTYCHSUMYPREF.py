n,m=map(int,input().split())
numbers=list(map(int,input().split()))




def sieve(N):
  s = [0 for _ in range(N + 1)]
  s[1] = 0
  s[2]=1
  i = 2

  for j in range(i * i, N + 1, i): s[j] = 1


  return s[1:]


def prefixsum(L):
  T = [0 for _ in range(len(L))]
  T[0] = L[0]
  for number in range(1, len(T)):
    T[number] = T[number - 1] + L[number]

  return T


def query(n,m):
  s = sieve(n)  # O(N * log2(log2(N)))
  s = prefixsum(s)  # O(N)

  ans = []
  for _ in range(m):
    x,y=map(int,input().split())
    if x == 0:
      ans.append(s[y])
    else:
      ans.append(s[y] - s[x - 1])
  return ans

resultlist=list(query(n,m))
for result in resultlist:
  print(result)











