import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_choices(player, ai):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print()
    print(Fore.GREEN + f"You chose: {choices[player]}" + Style.RESET_ALL)
    print(Fore.RED + f"AI chose: {choices[ai]}" + Style.RESET_ALL)
    print()

def player_choice():
    move = 0
    while move not in [1, 2, 3]:
        try:
            move = int(input(Fore.YELLOW + "Choose (1=Rock, 2=Paper, 3=Scissors): " + Style.RESET_ALL))
            if move not in [1, 2, 3]:
                print(Fore.RED + "Invalid choice! Enter 1, 2, or 3." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a number (1, 2, or 3)." + Style.RESET_ALL)
    return move

def ai_choice():
    return random.randint(1, 3)

def check_winner(player, ai):
    if player == ai:
        return "Draw"
    elif (player == 1 and ai == 3) or \
         (player == 2 and ai == 1) or \
         (player == 3 and ai == 2):
        return "Player"
    else:
        return "AI"

def rock_paper_scissors():
    print(Fore.CYAN + "Welcome to Rock-Paper-Scissors!" + Style.RESET_ALL)
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        player = player_choice()
        ai = ai_choice()
        display_choices(player, ai)
        winner = check_winner(player, ai)

        if winner == "Draw":
            print(Fore.CYAN + "It's a draw!" + Style.RESET_ALL)
        elif winner == "Player":
            print(Fore.GREEN + f"Congratulations {player_name}, you win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "AI wins this round!" + Style.RESET_ALL)

        play_again = input(Fore.YELLOW + "Do you want to play again? (yes/no): " + Style.RESET_ALL).lower()
        if play_again != 'yes':
            print(Fore.CYAN + "Thanks for playing Rock-Paper-Scissors!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    rock_paper_scissors()