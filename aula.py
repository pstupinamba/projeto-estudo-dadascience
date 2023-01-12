import matplotlib.pyplot as plt

#x = [1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
#y = [119011052,121154159,123774229,126403352,129025577,131639272,134228492,136780739,139280140,141714953,144090756,146825475,148684120,151556521,153726463,155822296,157070163,159636297,161790182,163947436,169799170,172385776,174632932,176876251,179108134,184184074,186770613,189335191,189612814,191481045,190755799,192379287,193976530,201062789,202799518,204482459,206114067]


dados= open("populacao_brasileira.csv").readlines()

x = []
y = []

#len: pega quantas linhas
#range: cria lista de 0 ao tamanho final
for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

titulo = "Crescimento da população Brasileira 1980-2016"
eixox = "Ano"
eixoy = "População x 100.000.000"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.plot(x, y, color="k", linestyle="--") #"plotagem"
#plt.scatter(x, y, label = "Meus pontos", color='k', marker=".") #gráfico escala
plt.bar(x,y, color="#e4e4e4") #gráfico em barra


plt.legend()
#plt.show()
plt.savefig("figura02.png", dpi=300)