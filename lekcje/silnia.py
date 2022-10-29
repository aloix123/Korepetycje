def policz_silnia(number):
    if number<=1:
        return 1
    return number*policz_silnia(number-1)
print(policz_silnia(4))