operation = ''

while operation != "Sair":

    operation = input("Digite a operação [/] [*] [-] [+] ou [Sair]: ")
    
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")

    if numero1.isdigit() and numero2.isdigit() == True:
        if operation == "/":
            resultado = float(numero1) / float(numero2)
            print(f'Resultado: {float(numero1)} / {float(numero2)} = {resultado}')
        elif operation == "*":
            resultado = float(numero1) * float(numero2)
            # return 
            print(f'Resultado: {float(numero1)} * {float(numero2)} = {resultado}')
        elif operation == "-":
            resultado = float(numero1) - float(numero2)
            # return 
            print(f'Resultado: {float(numero1)} - {float(numero2)} = {resultado}')
        elif operation == "+":
            resultado = float(numero1) + float(numero2)
            # return 
            print(f'Resultado: {float(numero1)} + {float(numero2)} = {resultado}')
        elif operation == "Sair" or "sair":
            print("FIM!")
            break 
        else:
            print(f'Operação inválida!')

    else:
        if numero1.isdigit() == False:
            print(f'Resultado: {numero1} não é um número!')
        if numero2.isdigit() == False:
            print(f'Resultado: {numero2} não é um número!')