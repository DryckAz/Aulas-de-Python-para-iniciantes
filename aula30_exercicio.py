"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero = int(numero_str)
    if numero % 2 == 0:
        print(f'O número {numero} é PAR.')
    else:
        print(f'O número {numero} é ÍMPAR.')
except ValueError:
    print('Isso não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
while True:  # Loop infinito, vai repetir até encontrar um valor válido
    
    try:
        hora = float(input("Que horas são? "))

        # Se digitar 24, tratamos como 0
        if hora == 24:
            hora = 0

        if hora < 0 or hora > 24:
            print("Hora inválida. Digite um número entre 0 e 24.")
            continue  # volta para o início do loop
        elif 0 <= hora < 12:
            print("Bom dia!")
        elif 12 <= hora < 18:
            print("Boa tarde!")
        else:  # de 18 até 23.999...
            print("Boa noite!")
        break  # se chegou até aqui, a hora está correta, sai do loop
    except ValueError:
        print("Por favor, digite um número válido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# Pede o primeiro nome do usuário
nome = input("Digite seu primeiro nome: ").strip()

# Verifica o tamanho do nome
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif 5 <= tamanho <= 6:
    print("Seu nome é normal")
else:  # maior que 6
    print("Seu nome é muito grande")
