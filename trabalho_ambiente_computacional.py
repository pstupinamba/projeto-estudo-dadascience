#Neste estudo de caso, faremos a comparação entre duas sequências de DNA: (1) ser humano; vs. (2) bactéria.
#DNA é uma molécula presente em todos os seres vivos, que é responsável por armazenar as características hereditárias. Ela é composta por sequências de nucleotídeos, que podem de quatro tipos: adenina, timina, citosina ou guanina. 
#"Computacionalmente" falando podemos representá-los através de 4 letras: A, T, C ou G.
#Neste estudo de caso, queremos avaliar se estruturas com funções parecidas (estamos usando sequências de RNA ribossomal) de organismos diferentes têm diferenças. Para isso vamos avaliar a quantidade de pares de nucleotídeos.

#DNA bactéria
""" entrada = open("./dados/bacteria.fasta").read()
saida = open("bacteria.html","w") """

#DNA humano
entrada = open("./dados/human.fasta").read()
saida = open("human.html","w")

cont = {}

for i in ['A', 'T', 'C' , 'G']:
    for j in ['A', 'T', 'C' , 'G']:
        cont[i+j] = 0

for k in range(len(entrada)-1):
    par = entrada[k]+entrada[k+1]
    if par in cont:
        cont[entrada[k]+entrada[k+1]] += 1
    
#print(cont)

#html

i = 1
for k in cont:
        transparencia = cont[k]/max(cont.values())
        saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color: rgba(0, 0, 0,"+str(transparencia)+")'>"+k+"</div>")
        
        if i%4 == 0: 
            saida.write("<div style='clear:both;'></div>")
            
        i+=1
        
saida.close()
        
        