"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Fase Pratica - A1
Codigo relativo a secao: 1.1 Numpy
Candidata: Nicole Cardozo dos Santos 
"""

import numpy as np
import math

#4. Iteracao em um Numpy array
#item a)
media = 0
cont = 0
arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
for num in arr:
    media += num
    cont +=1
media = round(media/cont, 2)
print("Media calculada com iteracao: ", media)

#item b)
dp = 0
for num in arr:
    dp += (num - media)**2
dp = round(math.sqrt(dp/cont), 2)
print("Desvio padrao calculado com iteracao:", dp)

#5. Funcoes Facilitadoras
#item a)
arr.sort()
print("Vetor ordenado: ", arr)

#item b)
print("Dimensoes do vetor: ", arr.shape[0])

#item c)
print("Media calculada com o metodo .mean(): ", round(arr.mean(), 2))

#item d)
print("Desvio padrao com o metodo .std(): ", round(arr.std(), 2))
print("Maior numero com o metodo .max(): ", arr.max())
print("Menor numero com o metodo .min(): ", arr.min())

#item e)
from numpy import random
lista = []
for i in range(100):
    lista.append(random.randint(11))
arr = np.array(lista)
print("Vetor criado com random: ", arr)
print("Media: ", round(arr.mean(), 2))
print("Desvio padrao: ", round(arr.std(), 2))
print("Maior valor: ", arr.max())
print("Menor valor: ", arr.min())