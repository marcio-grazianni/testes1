# Utilização:
# python argumentos 8 0
# python argumentos 8 30

import sys

linha = '-' * 80
argumentos = sys.argv
total_argumentos = len(argumentos)

print(linha)
print('argumentos:', argumentos)
print('type(argumentos):', type(argumentos))
print(linha)

print("Total de argumentos passados:", total_argumentos)
print(linha)

print("Nome do script Python:", argumentos[0])
print(linha)

if total_argumentos == 1:
    print("Nenhum argumento passado.")
else:
    print("Argumentos passados:")
    for contador in range(1, total_argumentos):
        print(f'argumentos[{contador}] =', argumentos[contador])
print(linha)
