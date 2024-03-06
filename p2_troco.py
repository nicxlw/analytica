"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Tarefa de Programacao - P2
Questao 3: Calculadora de troco
Candidata: Nicole Cardozo dos Santos 
"""

opcoes = [[100, 50, 20, 10, 5, 2, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while True:
    try:
        din = input()
        if '.' not in din or len(din.split('.')[1]) != 2: #se nao tiver duas casas decimais, gera um erro
            raise ValueError
        din = float(din) #se a entrada nao for um valor numerico, gera um erro
        break
    except ValueError:
        print("Erro: Input invalido.")
        
    
for i in opcoes[0]: # i é cada opcao de nota/moeda, comecando pelo 100
    j = opcoes[0].index(i)
    while round(din - i, 2) >= 0: #enquanto for possivel, reduzir i do valor de troco
        din = round(din - i, 2) 
        opcoes[1][j] += 1 #opcoes[1] é um contador de cada tipo de notas/moedas utilizadas
    if din == 0: #encerrar quando o troco chegar a 0
        break

print("NOTAS:")
for i in range(6): #opcoes de notas
    print(f"{opcoes[1][i]} nota(s) de R$ {opcoes[0][i]}.00")

print("\nMOEDAS:")
for i in range(6, 12): #opcoes de moedas
    print(f"{opcoes[1][i]} moeda(s) de R$ {opcoes[0][i]}")