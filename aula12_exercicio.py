#Exercício: Preciso criar um sistema básico onde exibe o imc do cliente.
#IMC = peso/ altura*altura

Nome = 'Endrick Azeitona'
Altura = 1.74
Peso = 78
imc = Peso / (Altura * Altura)

print('Olá', Nome, 'Seja bem vindo ao cosultório AzNutri!')
print('O cliente tem', Altura, 'e pesa', Peso, 'Kg', end='.\n')
print('Seu IMC é:', imc)
