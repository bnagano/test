import os

lista_compras = []

while True:
    operation = input("Digite a opção:\n[a]dicionar, [r]emover, [l]istar: ")
    operation.lower()
    if operation.isdigit() == False:
        os.system('clear')
        if operation == "a":
            adicionar = input("Digite o item para adicionar: ")
            lista_compras.append(adicionar)
        elif operation == "r":
            remover = input("Digite o indice para remover: ")
            lista_compras.pop(int(remover))
        elif operation == "l":
            os.system('clear')
            if lista_compras == []:
                print("Lista vazia!")
            else:
                for indice, nome in enumerate(lista_compras):
                    print(indice, nome)
        else:

            print("Digite uma opção valida!")