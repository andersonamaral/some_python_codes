__author__ = 'anderson.amaral@usp.br'

import math


#v = float(raw_input('digite a velocidade, que sera multiplicada por 10**8:'))*10**8
#print v
c = 3*(10**(8))
constant = 5.670373*(10**(-8))
t = 24*3600*365
M = 2*(10**30)

result = []


T = float(raw_input('digite a temperatura em Kelvins '))
R = float(raw_input('digite o raio da estrela'))*10**8


#Lei de Stefan

import matplotlib.pyplot as plt
import numpy as np


def massa_perdida_da_estrela():
    result = []
    for t in np.arange(0.0,90.0):


      L = float(4*3.14*(R**2)*constant*(T**4))

    #print "L:"
    #print L

#L = (d/dt)*(m*(c**2)), entao dt/dm = L/(c**2) . Chamando a taxa de perda de massa de uma estrela como "perda de massa por segundo:
    #print "Perda de massa por segundo:"

    perda_de_massa_por_segundo = float(L/(c**2))

    #print perda_de_massa_por_segundo

    print "Perda de massa por ano:"
#(dt/dm)*t

    perda_de_massa_por_ano = perda_de_massa_por_segundo*t


    print perda_de_massa_por_ano

#Tempo para a estrela se consumir totalmente, dada a massa da estrela como 2,0 * 10**(30)kg

    f = perda_de_massa_por_ano/M

    print f

#Assim, se quisermos saber quando a estrela se esgotara, basta colocar f = 1  => M/dm/dt = t

    fim_da_estrela = (M/perda_de_massa_por_segundo)/(t)

    print fim_da_estrela



result1 = massa_perdida_da_estrela()

print "\n"

print "Obviamente esses calculos nao servem para prever o fim da estrela, uma vez que outros fatores envolvidos influenciam muito antes do fim do ciclo da mesma"
