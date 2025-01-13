from random import randint

def main():
    while True:
        try:
            nr_user = int(input("Write a number from 1 to 10: "))
            nr_program = randint(1, 10)

            if nr_user == nr_program:
                print("You win!")
            elif nr_user < 1:
                print("The number is too small. Try again.")
            elif nr_user > 10:
                print("The number is too big. Try again.")
            else:
                print(f"You lose. I was thinking about {nr_program}.")
        except ValueError:
            pass

if __name__ == '__main__':
    main()
