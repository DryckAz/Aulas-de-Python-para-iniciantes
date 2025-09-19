# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123456'

if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Senha: ')
    if senha_digitada == senha_permitida:
        print('Seja bem-vindo!')
    else:
        print('A senha está incorreta!')    
elif entrada not in ['E','e','S','s']:
    print('Você não selecionou corretamente!')
else:
    print('Você está saindo!')

# Avaliação de curto circuito
#print(True and False and True)
#print(True and 0 and True)