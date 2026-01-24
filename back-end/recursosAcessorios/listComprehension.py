#Forma simplificada de gerar listas
array = [elemento+1 for elemento in range(1,10) if elemento > 2]
print(array) #[4, 5, 6, 7, 8, 9, 10]


#Forma "normal" de escrever o codigo
array2 = []
for elemento in range(1, 10):
    if elemento > 2:
        array2.append(elemento+1)
print(array2) #[4, 5, 6, 7, 8, 9, 10]

#MESMO RESULTADO