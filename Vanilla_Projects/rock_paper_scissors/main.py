from pkg import movements as mv

# Entry point for project

def run():
    player_score, cpu_score = mv.game()
    mv.game_winner(player_score, cpu_score)

    print("*****" * 5 + " Gracias por jugar al juego " + "*****" * 5)


if __name__ == "__main__":
    run()