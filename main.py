nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome != '' and idade != '':
    print(f'Seu nome eh {nome}')
    print(f'Seu nome invertido eh {nome[::-1]}') #invertido
    if ' ' in nome: 
        print(f'Seu nome contem espacos')
    else:
        print(f'Seu nome nao contem espacos')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome eh {nome[0]}')
    print(f'A ultima letra do seu nome eh {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')