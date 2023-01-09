import roman_numbers as rn

print(rn.I)

numero_romano = input('Digite um numero romano: ')
numero_inteiro = 0

if numero_romano.isdigit() == False:
    
    for indice in numero_romano:
        
        if indice == 'M':
            if indice[+1] < rn.M:
                numero_inteiro += rn.CM
            else:
                numero_inteiro += rn.M
            continue
        if indice == 'CM':
            numero_inteiro += rn.CM
            continue
        if indice == 'D':
            numero_inteiro += rn.D
            continue
        if indice == 'C':
            numero_inteiro += rn.C
            continue
        if indice == 'XC':
            numero_inteiro += rn.XC
            continue
        if indice == 'L':
            numero_inteiro += rn.L
            continue
        if indice == 'XL':
            numero_inteiro += rn.XL
            continue
        if indice == 'X':
            numero_inteiro += rn.X
            continue
        if indice == 'IX':
            numero_inteiro += rn.IX
            continue
        if indice == 'V':
            numero_inteiro += rn.V
            continue
        if indice == 'IV':
            numero_inteiro += rn.IV
            continue
        if indice == 'I':
            numero_inteiro += rn.I
            continue


        




        # if 'I' in numero_romano and len(numero_romano) < 4:
        #     numero_inteiro += 1
        #     indice = indice +1
        # else:
        #     print(f'{numero_romano} nao eh numero romano')
        #     break

        
    
else:
    print('Digite um numero romano')

if numero_inteiro > 0:
        print(f'{numero_romano} = {numero_inteiro}')