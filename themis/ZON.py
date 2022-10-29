n=int(input())
garden=input()
q=int(input())
kwiatek="#"
puste="."
numergarden=[]
for grzondka in garden:
    if grzondka==kwiatek:
        numergarden.append(1)
    else:
        numergarden.append(0)
print(numergarden)
def prefixsum(L):
  T = [0 for _ in range(len(L))]
  T[0] = L[0]
  for number in range(1, len(T)):
    T[number] = T[number - 1] + L[number]

  return T

def query(m,q):

  s = prefixsum(m)
  print(s)# O(N)

  ans = []
  for _ in range(q):
    x,y=map(int,input().split())
    if x == 0:
      ans.append(s[y-1])
    else:
      ans.append(s[y-1] - s[x -1]+1)
  return ans
resultlist=list(query(numergarden,q))
for result in resultlist:
  print(result)