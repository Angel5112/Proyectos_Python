# Funciones del projecto de ROCK, PAPER y SCISSORS

import random

# Funcion para aplicar los movimientos de la cpu

def cpu_movements():
    moveset = {
        1: "piedra",
        2: "papel",
        3: "tijeras" 
    }

    action = random.randint(1, 3)
    return moveset[action].title()


# Funcion para determinar ganador de la ronda

def round_winner(player, cpu):
    if player == cpu:
        return 0
    elif player == "piedra" and cpu == "tijeras":
        return 1
    elif player == "papel" and cpu == "piedra":
        return 1
    elif player == "tijeras" and cpu == "papel":
        return 1
    else:
        return 2
    

# Funcion para jugar el juego

def game():
    player_score = 0
    cpu_score = 0
    
    while player_score < 3 or cpu_score < 3:
        player_move = input("Piedra, Papel o Tijeras? ")
        player_move = player_move.lower()

        if player_move != "piedra" or player_move != "papel" or player_move != "tijeras":
            print("Error: Movimiento ingresado es invalido... Punto para la CPU!\n")
            cpu_score += 1
        else:
            cpu_move = cpu_movements()
            player_move = player_move.title()
            print(cpu_move)

            round = round_winner(player_move, cpu_move)
            if round == 0:
                print("Empate!\n")
            elif round == 1:
                print("Punto: Jugador\n")
                player_score += 1
            else:
                print("Punto: CPU\n")
                player_score += 1

    return player_score, cpu_score


# Funcion para determinar el ganador del juego

def game_winner(player_score, cpu_score):
    if player_score > cpu_score:
        print(f"Ganador: Jugador ({player_score} pts)!\n")
    else:
        print(f"Ganador: CPU ({cpu_score} pts)!\n")
