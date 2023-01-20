import random
import os

jokempo = ["Pedra", "Papel", "Tesoura"]

while True:
    print("JOKEMPO!")
    jogador = input("Escolha sua opcao (Pedra, Papel, Tesoura): ")
    maquina = random.choice(jokempo)
    if jogador == "Pedra" or "Papel" or "Tesoura":
        os.system('clear')
        if jogador == "Pedra" and maquina == "Pedra":
            print(f"{jogador} x {maquina} = EMPATE!")
        elif jogador == "Pedra" and maquina == "Papel":
            print(f"{jogador} x {maquina} = VOCE PERDEU!")
        elif jogador == "Pedra" and maquina == "Tesoura":
            print(f"{jogador} x {maquina} = VOCE VENCEU!")
        elif jogador == "Tesoura" and maquina == "Pedra":
            print(f"{jogador} x {maquina} = PERDEU!")   
        elif jogador == "Tesoura" and maquina == "Tesoura":
            print(f"{jogador} x {maquina} = EMPATE!")
        elif jogador == "Tesoura" and maquina == "Papel":
            print(f"{jogador} x {maquina} = VOCE VENCEU!")
        elif jogador == "Papel" and maquina == "Papel":
            print(f"{jogador} x {maquina} = EMPATE!")
        elif jogador == "Papel" and maquina == "Pedra":
            print(f"{jogador} x {maquina} = VENCEU!")
        elif jogador == "Papel" and maquina == "Tesoura":
            print(f"{jogador} x {maquina} = PERDEU!")
    else:
        print("Opcao indisponivel")
    
    
    
    
    
