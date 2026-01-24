# Gera lista de 1 a 10
array = [i for i in range(1, 10)]

# Função lambda default
maisUm = lambda x : x + 1
print(maisUm(1))

# Função lambda aplicada com map (nao chama "duplicados(array)" pois o map ja informa o array como referencia após a virgula)
duplicados = map(lambda numero: numero * 2, array)
print(list(duplicados))