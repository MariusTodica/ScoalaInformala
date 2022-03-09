import random


def ask_name():
    active = True

    name = input("Enter your name: ").title()
    message = input(f"Hi {name}! Welcome to Rock-Paper-Scissors. \nYou wanna play?[y/n]: ")

    if message == 'n':
        return False
    else:
        return active


def game():
    active = True

    while active:
        print("1. Rock \n2. Paper \n3. Scissors")

        turn = {
            1: 'rock',
            2: 'paper',
            3: 'scissors'
        }
        val = list(turn.values())
        human_turn = input("Enter an option from the list above: ")

        if human_turn == '1' or human_turn == "rock":
            human_turn = val[0]
        elif human_turn == '2' or human_turn == "paper":
            human_turn = val[1]
        elif human_turn == '3' or human_turn == "scissors":
            human_turn = val[2]
        else:
            game()

        robot = random.choice(val)

        print("-------------------------------")
        print(f"Robot has chosen {robot}.")
        print("-------------------------------")
        print(f"You have chosen {human_turn}.")
        print("-------------------------------")

        if robot == "rock" and human_turn == "rock":
            print("Tie!")
            return game()
        elif robot == "paper" and human_turn == "paper":
            print("Tie!")
            return game()
        elif robot == "scissors" and human_turn == "scissors":
            print("Tie!")
            return game()
        elif robot == "rock" and human_turn == "paper":
            print("You won!")
        elif robot == "paper" and human_turn == "rock":
            print("Robot won")
        elif robot == "rock" and human_turn == "scissors":
            print("Robot won!")
        elif robot == "scissors" and human_turn == "rock":
            print("You won!")
        elif robot == "paper" and human_turn == "scissors":
            print("You won!")
        elif robot == "scissors" and human_turn == "paper":
            print("Robot won!")

        again = input("You want to play again?[y/n]: ")
        if again == 'y':
            return game()
        else:
            print("Game over!")
            exit()


if __name__ == '__main__':
    ask_name()
    game()
