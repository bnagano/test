nome = input('Digite seu nome: ')
nova_string = ''

for i in range(len(nome)):
    nova_string += (nome[i] + '*')

print(nova_string)