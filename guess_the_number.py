from random import randint

def main():
    min_num = 1
    max_num = 100
    attempts = 1
    number = randint(min_num, max_num)

    while True:    
        try:
            guess = int(input("Guess a number between {} and {}: ".format(min_num, max_num)))

            if guess == number:
                print(f"You guessed the correct number! Attempts: {attempts}.")
                break
            elif guess < number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
            
            attempts += 1
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
