"""
Processo Seletivo 2024.1 - UFRJ Analytica
Equipe de Desenvolvimento - Fase Pratica - A1
Codigo relativo as secoes: 1.2.2 Parte Pratica, 1.3 Matplotlib, 1.4 Desafio Final
Candidata: Nicole Cardozo dos Santos 
"""

#-----parte prática-----
import pandas as pd

#item 1
df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

#item 2
print(df)

#item 3
df_91 = df[df["ano"] == 1991]
media =  df_91["idhm"].mean()
print("IDH medio do brasil em 1991:", round(media, 3))

#item 4
df_acima = df_91[df_91["idhm"] > media ]
print("Estados com IDH acima da media:", df_acima["sigla_uf"].values)

#item 5
df_ordenado = df_91.sort_values(by="idhm", ascending=False)
print("5 estados com maior IDH em 1991: \n", df_ordenado.head(5))

#item 6 (usando idxmin e idxmax)
uf_menor_idh = df_91.loc[df_91["idhm"].idxmin(), "sigla_uf"]
print("estado com menor idh usando .idxmin():", uf_menor_idh)
uf_maior_idh = df_91.loc[df_91["idhm"].idxmax(), "sigla_uf"]
print("estado com maior idh usando .idxmax():", uf_maior_idh)

#item 6 (usando min e max)
uf_menor_idh = df_91[df_91["idhm"] == df_91["idhm"].min()]["sigla_uf"].values[0]
print("estado com menor idh usando .min():", uf_menor_idh)
uf_maior_idh = df_91[df_91["idhm"] == df_91["idhm"].max()]["sigla_uf"].values[0]
print("estado com maior idh usando .max():", uf_maior_idh)

#-----matplotlib-----
import matplotlib.pyplot as plt

#item 1
plt.bar(df_91["sigla_uf"], df_91["populacao_urbana"])
plt.ticklabel_format(style='plain', axis='y') #marcadores do eixo y em formato simples (sem notação científica)
plt.show()

#item 2
df_00 = df[df["ano"] == 2000]
df_10 = df[df["ano"] == 2010]
plt.hist(df_91["idhm"], alpha=0.5, label='1991') #alpha=0.5 para melhorar a visibilidade
plt.hist(df_00["idhm"], alpha=0.5, label='2000')
plt.hist(df_10["idhm"], alpha=0.5, label='2010')
plt.legend()
plt.show()

#item 3
plt.scatter(df["idhm"], df["expectativa_vida"])
plt.show()
print("O gráfico demonstra de forma clara que quanto mais alto o IDH, mais alta a expectativa de vida dos habitantes")

#-----desafio final-----
dif_list= [] #diferenca de cada estado entre 1991 e 2010
maior_10 = [] #estados com diferenca >=  10

for i in range(27): #numero de estados
    diferenca = df_10.loc[i+54, "expectativa_vida"] - df_91.loc[i, "expectativa_vida"]
    dif_list.append(diferenca)
    if(diferenca >= 10):
        maior_10.append(df_91.loc[i, "sigla_uf"])

plt.bar(df_91["sigla_uf"], dif_list)
plt.show()

print("estados que tiveram um aumento de pelo menos 10 anos na expectativa de vida entre 1991 e 2010:", maior_10)