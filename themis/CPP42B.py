q=input()
g=input().lower()
W=[]
for letter in g:
   W.append(ord(letter))
wc=set(W)
f={}
for g in wc:
    f[g]=0
for letter in W:
    f[letter]+=1
resultcount=max(list(f.values()))
resultletter=''
for h in f:
    if f[h]==resultcount:
        resultletter=chr(h)
print(f"{resultcount} {resultletter}")

