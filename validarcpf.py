import re
import sys
entrada = input("Digite um cpf: ")
cpf = re.sub(
    r'[^0-9]', '', entrada    
)

primeiro_char_repetido = entrada == entrada[0] * len(entrada)

if primeiro_char_repetido:
    print("Voce digitou dados sequenciais! ")
    sys.exit()

multiplicador1 = 10
multiplicador2 = 11
cpf_novo = cpf[:9]
total1 = 0
total2 = 0

for numero1 in cpf_novo:
    total1 += int(numero1) * multiplicador1
    multiplicador1 -= 1

digito1 = (total1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
    
cpf_novo += str(digito1)

for numero2 in cpf_novo:
    total2 += int(numero2) * multiplicador2
    multiplicador2 -= 1

digito2 = (total2 *10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_novo += str(digito2)

if cpf_novo == cpf:
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")