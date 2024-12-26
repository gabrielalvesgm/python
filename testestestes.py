numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [1, 3, 5, 7, 9]
pares = [2, 4, 6, 8, 10]

for x in numeros:
    if x in impares:
        print(f"Este número {x} é ímpar")
    else:
        print(f"Este número {x} é par")