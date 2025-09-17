nome = 'Endrick Eduardo'
sobrenome = 'de Azevedo Azeitona'
idade = 27
ano_nascimento = 1998
maior_de_idade = idade >= 18
altura_metros = 1.74


print('Nome:', nome, sobrenome)
print('Idade:', idade)
print('Altura:', altura_metros)
print('O candidato é maior de idade?:')
if idade >=18:
    print('Sim')
else:
    print('Não')
if maior_de_idade:
    print('Você está apto para se inscrever.')
else:
    print('Você não está apto para se inscrever.')        