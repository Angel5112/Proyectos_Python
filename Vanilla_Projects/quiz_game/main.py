# Quiz Game = Hacer 10 preguntas al usuario y dependiendo de si acierta la pregunta, se sumara 1 punto, al final mostrar cuantas preguntas acerto */10

from pkg import questions

def run():
    name = input("\nIngrese su nombre: ")
    score = questions.quiz_game()
    print(f"{name} ha conseguido responder {score}/10 preguntas!")


if __name__ == '__main__':
    run()