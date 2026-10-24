import random
print("""
THIS IS A ROCK, PAPER, SCISSORS GAME
YOU CAN ONLY PLAY AGAINST THE COMPUTER 
TWO RULES:
1. YOU INPUT WHATEVER ELEMENT YOU WANT OF THE 3
ROCK ==> R ; PAPER ==> P ; SCISSORS ==> S
2. YOU PLAY A GAME OF THREE SETS, THE PLAYER WITH THE HIGHEST AMOUNT OF POINTS IN 3, WINS!
""")
option = ["Rock", "Scissors", "Paper"]
code = True
game_set = 0
game_round = 1
computer_total = 0
player_total = 0
computer_score = 0
player_score = 0
while code:
    request = input("Do you want to play? yes or no: ").lower()
    player_total = 0
    computer_total = 0
    if request != "yes" and request != "no":
        print("Wrong input, PLEASE INPUT \"yes\" OR \"no\" ")
    if request == "no":
        quit()
    if request == "yes":
        player_name = input("Please enter your name: ").capitalize()
        while game_set <= 3:
            request = " "
            choice = random.choice(option)
            print("PLEASE INPUT ===. R FOR ROCK. S FOR SCISSORS, P FOR PAPER")
            start = input("Rock, Paper, Scissors: ").upper()
            if choice == "Rock" and start == "R":
                print(f"Computer chose {choice}")
                print("Draw")
                print(f"Computer {computer_score}: {player_score} {player_name} ")
            if choice == "Scissors" and start == "S":
                print(f"Computer chose {choice}")
                print("Draw")
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Paper" and start == "P":
                print(f"Computer chose {choice}")
                print("Draw")
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Rock" and start == "S":
                print(f"Computer chose {choice}")
                print("Computer wins")
                computer_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Scissors" and start == "R":
                print(f"Computer chose {choice}")
                print(f"{player_name} wins")
                player_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Paper" and start == "R":
                print(f"Computer chose {choice}")
                print("Computer wins")
                computer_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Rock" and start == "P":
                print(f"Computer chose {choice}")
                print(f"{player_name} wins")
                player_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Paper" and start == "S":
                print(f"Computer chose {choice}")
                print(f"{player_name} wins")
                player_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if choice == "Scissors" and start == "P":
                print(f"Computer chose {choice}")
                print("Computer wins")
                computer_score += 1
                print(f"Computer {computer_score} : {player_score} {player_name} ")
            if computer_score == 3:
                computer_total += 1
            if player_score == 3:
                player_total += 1
            if computer_score == 3 or player_score == 3:
                game_set += 1
                computer_score = 0
                player_score = 0
                print(f"After {game_set} set --> Computer {computer_total} : {player_total} {player_name}")
            if game_set == 3:
                game_set = 0
                if computer_total > player_total:
                    print(f"{player_name} looses")
                else:
                    print(f"{player_name} wins")
                break
# I have finally added my first code to Github