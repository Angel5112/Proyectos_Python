# Funciones para el quiz game

def quiz_game():
    questions_answers = {
        'Cual es el nombre del creador del juego?':'angel patino',
        'Quien es el jugador de futbol con mas balones de oro?':'lionel messi',
        'Que equipo gano la ultima UEFA Champions League?':'real madrid',
        'Que GPU piensa comprarse el autor del juego?':'nvidia 1070 ti',
        'Que CPU piensa comprarse el autor del juego?':'ryzen 7 2700x',
        'En que lenguaje de programacion esta hecho el juego?':'python',
        'Que equipos jugaran la final de la EFL Cup en la Premier League?':'manchester united y newcastle',
        'Quien es el jugador de basquetball con mas puntos en la historia?':'lebron james',
        'Que seleccion gano la ultima UEFA Euro Cup?':'italia',
        'En que universidad estudio el autor del juego?':'ucab'
    }

    score = 0

    for element in questions_answers:
        question = element
        print(question)
        user = input()
        print(f"La respuesta es: {questions_answers[question].title()}")

        if user.lower() == questions_answers[question]:
            score += 1
            print('Tu respuesta es correcta!\n')
        else:
            print(f"Tu respuesta es incorrecta!\n")
    
    return score
