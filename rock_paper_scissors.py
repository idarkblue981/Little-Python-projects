from random import choice

def main():
    options = ["rock", "paper", "scissors"]

    while True:
        try:
            user = input("Choose between 'rock', 'paper' and 'scissors': ").strip().lower()

            if user not in options:
                raise ValueError

            program = choice(options)

            if user == program:
                print('Tie.')
            if (user == "rock" and program == "paper") or (user == "paper" and program == "scissors") or (user == "scissors" and program == "rock"):
                print("I win.")
            if (user == "rock" and program == "scissors") or (user == "paper" and program == "rock") or (user == "scissors" and program == "paper"):
                print("You win.")
        except ValueError:
            print("You can only choose between 'rock', 'paper' and 'scissors'!")
        
if __name__ == '__main__':
    main()
