def main():
    guess_the_number()

def guess_the_number():
    import random
    min_num = 1
    max_num = 100
    number = random.randint(min_num, max_num)
    while True:    
        try:
            guess = int(input("Guess a number between {} and {}: ".format(min_num, max_num)))
            if guess == number:
                print("You guessed the correct number!")
                break
            elif guess < number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        except ValueError:
            pass

if __name__ == '__main__':
    main()
