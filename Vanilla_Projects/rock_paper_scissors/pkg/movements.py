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
    elif player == "piedra" and cpu == "papel":
        return 2
    elif player == "papel" and cpu == "piedra":
        return 1
    elif player == "papel" and cpu == "tijeras":
        return 2
    elif player == "tijeras" and cpu == "papel":
        return 1
    elif player == "tijeras" and cpu == "piedra":
        return 2
    

# Funcion para jugar el juego

def game():
    player_score = 0
    cpu_score = 0
    player_moveset = ['piedra', 'papel', 'tijeras']
    
    while player_score < 2 and cpu_score < 2:
        player_move = input("Piedra, Papel o Tijeras? \n")
        player_move = player_move.lower()

        if player_move not in player_moveset:
            print("Error: Movimiento ingresado es invalido... Punto para la CPU!\n\n")
            cpu_score += 1
        else:
            cpu_move = cpu_movements()
            print(cpu_move)
            cpu_move = cpu_move.lower()

            round = round_winner(player_move, cpu_move)
            if round == 0:
                print("Empate!\n")
            elif round == 1:
                print("Punto: Jugador\n")
                player_score += 1
            else:
                print("Punto: CPU\n")
                cpu_score += 1

    return player_score, cpu_score


# Funcion para determinar el ganador del juego

def game_winner(player_score, cpu_score):
    if player_score > cpu_score:
        print(f"Ganador: Jugador ({player_score} pts)!\n")
    else:
        print(f"Ganador: CPU ({cpu_score} pts)!\n")
