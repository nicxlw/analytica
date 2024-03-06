"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Tarefa de Programacao - P2
Questao 4: Frequencia de numeros
Candidata: Nicole Cardozo dos Santos 
"""

numeros = [[],[]]

while True:
    num = input()
    if num == 'f':
        break

    # defesa do codigo
    try:
        if '.' in num: #se o usuario digitar um float, gera um erro
            raise ValueError
        num = int(num) #se o usuario digitar uma entrada nao numerica, gera um erro
    except ValueError:
        continue
    #-------

    if num not in numeros[0]: #numeros[0] funciona como lista de entradas validas inseridas pelo usuario
        numeros[0].append(num)
        numeros[1].append(0)
    j = numeros[0].index(num) #index do valor correspondente a entrada
    numeros[1][j] += 1   #numeros[1] funciona como um contador dos valores de numeros[0] 
for i in range(len(numeros[0])):
    print(f'O numero {numeros[0][i]} apareceu {numeros[1][i]} vez(es)')
print("Fim...")