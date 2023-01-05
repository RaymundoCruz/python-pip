import random


def options():
    menu=('piedra','papel','tijeras') 
    option_user = input('Ingresa valores piedra, papel o tijeras:')
    option_user = option_user.lower()
    option_computer=random.choice(menu)
    if option_user not in menu:
        return None,None
    else:
        return option_user, option_computer

 
def juego(option_user, option_computer, score_user, score_computer):

    if option_computer == option_user:
        pass

    if option_user == "piedra" and option_computer == "tijeras":
        score_user=1

    elif option_user == "piedra" and option_computer == "papel":
        score_computer=1

    if option_user == "papel" and option_computer == "piedra":
        score_user=1

    elif option_user == "papel" and option_computer == "tijeras":
        score_computer=1

    if option_user == "tijeras" and option_computer == "papel":
        score_user=1
        
    elif option_user == "tijeras" and option_computer == "piedra":
        score_computer=1

    return score_user,score_computer


def run():
    score_user=0
    score_computer=0
    option_user,option_computer=options()
    print(f'User ha elegido : {option_user}, mientras que computer ha elegido: {option_computer}')
    score_user,score_computer= juego(option_user,option_computer, score_user, score_computer)
    if score_user == 1:
        print("gana user")
    elif score_computer == 1:
        print("gana computer")
    elif score_computer ==0 and score_user==0:
        print("Empate")


if __name__=='__main__':
    run()



