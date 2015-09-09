__author__ = 'anderson.amaral@usp.br'

# Verifica se um numero 'e primo ou nao

# Usuario digita numero abaixo
num = int(input("Digite um numero qualquer: "))

# numeros primos sempre sao maiores do que um
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"nao se trata de um numero primo")
           print(i,"vezes",num//i,"'e",num)
           break
   else:
       print(num," se trata de um numero primo")

#Sendo menor do que 1, certeza que nao se trata de numero primo
else:
   print(num,"nao se trata de um numero primo")