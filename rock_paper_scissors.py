def main():
    game()

def game():
    import random

    list = ['Rock', 'Paper', 'Scissors']

    while True:
        try:
            user = input('Choose between Rock, Paper and Scissors: ')
            program = random.choice(list)

            if user == 'Rock' and program == 'Rock':
                print('Tie.')
            elif user == 'Rock' and program == 'Paper':
                print('I win.')
            elif user == 'Rock' and program == 'Scissors':
                print('You win.')

            elif user == 'Paper' and program == 'Rock':
                print('You win.')
            elif user == 'Paper' and program == 'Paper':
                print('Tie.')
            elif user == 'Paper' and program == 'Scissors':
                print('I win.')

            elif user == 'Scissors' and program == 'Rock':
                print('I win.')
            elif user == 'Scissors' and program == 'Paper':
                print('You win.')
            elif user == 'Scissors' and program == 'Rock':
                print('Tie.')
            
        except ValueError:
            pass
        
if __name__ == '__main__':
    main()
