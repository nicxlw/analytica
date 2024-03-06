"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Tarefa de Programacao - P2
Questao 2: Movimentacao do cavalo no xadrez
Candidata: Nicole Cardozo dos Santos 
"""

horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['1', '2', '3', '4', '5', '6', '7', '8']

while True:
    entrada = input()

    # defesa do codigo
    if entrada == 'f':
        break
    if len(entrada) != 5:
        print("Erro: input invalido")
        continue
    if entrada[0] not in horizontal or entrada[1] not in vertical or entrada[3] not in horizontal or entrada[4] not in vertical or entrada[2] != ' ':
        print("Erro: input invalido")
        continue
    #------------

    x0 = horizontal.index(entrada[0]) #indice do x inicial
    y0 = int(entrada[1]) #y inicial
    xf = horizontal.index(entrada[3]) #indice do x final
    yf = int(entrada[4]) #y final

    difx = abs(xf-x0) #distancia entre x inicial e final
    dify =abs (yf-y0) #distancia entre y inicial e final

    if (difx == 2 and dify == 1) or (difx == 1 and dify == 2): #movimento "em L"
        print("VALIDO")
    else:
        print("INVALIDO")

print("Fim...")


