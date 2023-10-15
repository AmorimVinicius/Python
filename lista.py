# Exibir indices de uma lista

lista = ['Maria', 'José', 'Ana']
indices= range(len(lista))

print('Nomes da lista')
for nome in lista:
    print(nome)

print('\n\nIndíces da lista')
for indice in indices:
    print(indice, lista[indice])

print('\n\nTestando index')
print(lista.index('José'))