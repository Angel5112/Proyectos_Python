# Funciones del proyecto Choose your own adventure

# Funcion para decidir el final del juego

def ending_options(beg, midd, end):
    if beg == 'wake up' and midd == 'eat the food' and end == 'visit your family':
        print("\nCongratulations! You live a normal life!\n")
    elif beg == 'turn on the lights' and midd == 'get out without eating' and end == 'buy some stocks':
        print("\nYour life is rather unique!\n")
    elif beg == 'keep sleeping' and midd == 'order some food' and end == 'travel to another country':
        print("\nYou are living a one of a kind life!\n")
    else:
        print("\nSorry, but you do not qualify... maybe selecting the same array of options works better...?\n")



# Funcion para jugar el juego

def game():
    beginning = {
        "wake up": "You wake up in the darkness...",
        "turn on the lights": "You turn on the lights with your phone and wake out of bed...",
        "keep sleeping": "You sleep through the rest of the game..."
    }

    mid = {
        "eat the food": "You eat some bacon with eggs...",
        "get out without eating": "You get out without eating...",
        "order some food": "You order some food, it should arrive within 40 minutes...",
    }

    ending = {
        "visit your family": "You decide to visit your family...",
        "buy some stocks": "You put some money on the stock market...",
        "travel to another country": "You decide to travel to another country...",
    }

    while True:
        decision = int(input("Do you want go play the game? (1 = Yes, 0 = No)\n"))
        if decision == 1:
            action = input("\nWhat do you want to do?\n 1. Wake up\n 2. Turn on the lights\n 3. Keep sleeping ? \n\n")
            beg = action.lower()
            
            action = input("\nWhat do you want to do?\n 1. Eat the food\n 2. Get out without eating\n 3. Order some food\n\n")
            midd = action.lower()
            

            action = input("\nWhat do you want to do?\n 1. Visit your family\n 2. Buy some stocks\n 3. Travel to another country\n\n")
            end = action.lower()
            
            print("\n")
            print(beginning[beg])
            print(mid[midd])
            print(ending[end])

            ending_options(beg.lower(), midd.lower(), end.lower())
        else:
            print("\n" + "*****" * 5 + " Thanks for playing! " + "*****" * 5)
            break

