array = [0, 1, 2, 3, 4, 6, 7, 8, 9]

contador = 0

for i in array:
    if i != contador:
        n = i-1
        break
    else:
        contador += 1

print(n)        