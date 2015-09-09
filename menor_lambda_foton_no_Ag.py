"""__author__ = 'anderson.amaral@usp.br'


Menor comprimento de onda possivel para um foton
incidente no aluminio
"""

v = float(raw_input("digite a velocidade"))
c = 3*(10**8) #m/s
w = 4.2
hc = 1243*(10**9)

if v/c >= 0.1:
    Ec = ((0.511 * 10**6)*0.5)*((v/c)**2)
    print "A energia cinetica 'e de ", Ec , "ev"
    lambd = hc/(w + Ec)
    print "O comprimento de onda 'e ", lambd , "metros"
else:
    print "Esse nao 'e um problema relativistico : a relacao deve ser  v/c >= 0.1 "



