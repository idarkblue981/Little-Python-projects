from random import choice

def main():
    length_setting, numbers_setting, uppercase_setting, lowercase_setting = settings()
    generated_password = password_generator(length_setting, numbers_setting, uppercase_setting, lowercase_setting)
    print(generated_password)

def settings():
    while True:
        try:
            length_setting = int(input('Enter length (between 4 and 50): '))
            if length_setting < 4 or length_setting > 50:
                raise ValueError

            numbers_setting = input('Do you want numbers in your password (enter "Yes" or "No"): ')
            if numbers_setting not in {'Yes', 'No'}:
                raise NameError
            
            uppercase_setting = input('Do you want uppercase letters in your password (enter "Yes" or "No"): ')
            if uppercase_setting not in {'Yes', 'No'}:
                raise NameError
            
            lowercase_setting = input('Do you want lowercase letters in your password (enter "Yes" or "No"): ')
            if lowercase_setting not in {'Yes', 'No'}:
                raise NameError
            
            if numbers_setting == 'No' and uppercase_setting == 'No' and lowercase_setting == 'No':
                raise NameError

            return length_setting, numbers_setting, uppercase_setting, lowercase_setting
        except ValueError:
            print("Please enter a valid number between 4 and 50.")
        except NameError:
            print("Please enter 'Yes' or 'No'.")

def password_generator(length_setting, numbers_setting, uppercase_setting, lowercase_setting):
    characters = ''
    numbers = '1234567890'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'

    if numbers_setting == 'Yes':
        characters += numbers
    if uppercase_setting == 'Yes':
        characters += uppercase
    if lowercase_setting == 'Yes':
        characters += lowercase

    if not characters:
        raise ValueError("At least one character type should be included.")

    generated_password = ''.join(choice(characters) for _ in range(length_setting))
    return generated_password

if __name__ == "__main__":
    main()