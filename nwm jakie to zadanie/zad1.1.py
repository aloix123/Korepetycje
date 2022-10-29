# implementacja pseudokod
A = list(map(int, input().split(",")))
print(A)
n = int(input("s"))
wynik = 0
S = 0
for num in A:
    for x in A:
        if num - x != 0 and (num * x) % n != 0 and num * x > wynik:
            wynik = num * x
        print(num)
        print(x)
S = wynik
print(S)
