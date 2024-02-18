import re
import csv
import os

def get_user_input():
    name = input('Enter name: ')
    if not name:
        raise ValueError("Name cannot be empty.")
    
    phone_number = input('Enter phone number: ')
    return name, phone_number

def add_contact_to_csv(name, phone_number):
    with open("contact_book.csv", 'a', newline='') as file:
        writer = csv.writer(file)

        if os.path.getsize("contact_book.csv") == 0:
            writer.writerow(['Name', 'Phone Number'])

        writer.writerow([name, phone_number])
        print("Contact added to contact_book.csv.")

def main():
    while True:
        try:
            name, phone_number = get_user_input()

            if re.match(r'^\d+$', phone_number):
                add_contact_to_csv(name, phone_number)
            else:
                raise ValueError("Invalid phone number. Please enter a valid number.")

        except FileNotFoundError:
            print("Error: The file 'contact_book.csv' was not found.")
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()