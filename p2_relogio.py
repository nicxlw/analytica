"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Tarefa de Programacao - P2
Questao 1: Calculadora de angulo entre ponteiros do relogio
Candidata: Nicole Cardozo dos Santos 
"""

while True:
    horario = input()
    if horario == 'f':
        print('Fim...')
        break

    #defesa do codigo
    try:
        if len(horario) != 5: #se a entrda nao tiver 5 caracteres, gera um erro
            raise ValueError
        else: 
            hora = int(horario.split(':')[0])  #se a entrada nao tiver um ':' ou nao for numerica, gera um erro
            minuto = int(horario.split(':')[1])
            if hora > 23 or hora < 0 or minuto < 0 or minuto > 59 or horario.index(':') != 2: #se os valores de hora e minuto forem invalidos ou nao tiverem 2 digitos, gera um erro
                raise ValueError 
    except ValueError: 
        print("Input invalido.")
        continue
    #------

    hora = (hora % 12) * 30 # 30 graus por hora, partindo do 12
    minuto = minuto * 6 # 6 graus por minuto, partindo do 12
    ang = abs(hora - minuto)
    if ang > 180: #se nao for o menor angulo, pegar o angulo complementar (menor)
        ang = 360 - ang    
    print(f'O menor angulo e de {ang}°')
