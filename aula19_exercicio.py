#Exercício fazer um valor ser comparado com outro e aparecer o valor maior ou igual primeiro que o menor

valor_1 = input('Digite o primeiro valor:')
valor_2 = input('Digite o segundo valor:')

if valor_1 > valor_2:
    print('O valor', valor_1, 'é maior que', valor_2, '.')
elif valor_1 == valor_2:
    print('O valor', valor_1, 'é igual a', valor_2, '.')    
else:
    print('O valor', valor_2, 'é maior que', valor_1, '.')
