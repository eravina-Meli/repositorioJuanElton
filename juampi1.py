def max(naturales):
    winner = -1
    for n in naturales:
        if n > winner:
            winner = n
    return n

numeros = [-2, 4, 5, 6, 7]
print(max(numeros))