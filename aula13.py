Nome = 'Endrick Azeitona'
Altura = 1.74
Peso = 78
imc = Peso / (Altura * Altura)

"f-strings"
linha_1 = f'Olá {Nome}, seja bem vindo ao consultório AzNutri!'
linha_2 = f'O cliente tem {Altura}, e pesa {Peso} Kg.'
linha_3 = f'Seu IMC é: {imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)
