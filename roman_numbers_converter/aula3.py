import roman_numbers as rn

numero_romano = input('Digite um numero romano: ')
numero_inteiro = 0

if numero_romano.isdigit() == False:

    if "CM" in numero_romano:
        duplo = "CM"
        for i in range(0,len(duplo)):
            numero_romano = numero_romano.replace(duplo, "") 
        numero_inteiro += 900
    
    if "XC" in numero_romano:
        duplo = "XC"
        for i in range(0,len(duplo)):
            numero_romano = numero_romano.replace(duplo, "") 
        numero_inteiro += 90

    if "XL" in numero_romano:
        duplo = "XL"
        for i in range(0,len(duplo)):
            numero_romano = numero_romano.replace(duplo, "") 
        numero_inteiro += 40
    
    if "IX" in numero_romano:
        duplo = "IX"
        for i in range(0,len(duplo)):
            numero_romano = numero_romano.replace(duplo, "") 
        numero_inteiro += 9

    if "IV" in numero_romano:
        duplo = "IV"
        for i in range(0,len(duplo)):
            numero_romano = numero_romano.replace(duplo, "") 
        numero_inteiro += 4

    for indice in numero_romano:
        
        if indice == 'M':
            numero_inteiro += rn.M
            continue
        if indice == 'D':
            numero_inteiro += rn.D
            continue
        if indice == 'C':
            numero_inteiro += rn.C
            continue
        if indice == 'L':
            numero_inteiro += rn.L
            continue
        if indice == 'X':
            numero_inteiro += rn.X
            continue
        if indice == 'V':
            numero_inteiro += rn.V
            continue
        if indice == 'I':
            numero_inteiro += rn.I
            continue
    
else:
    print('Digite um numero romano')

if numero_inteiro > 0:
        print(f'{numero_romano} = {numero_inteiro}')