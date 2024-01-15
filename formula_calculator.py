def main():    # Main function to repeatedly get user input and perform calculations
    while True:
        formula, first_nr, last_nr = get_input()
        calculating(formula, first_nr, last_nr)


def get_input():    # Function to get user input for formula and number range
    while True:
        try:
            formula = input('Enter formula (use x as the variable): ')
            first_nr = int(input('Enter first number: '))
            last_nr = int(input('Enter last number: '))

            # Validate input range
            if last_nr < first_nr:
                raise ValueError("Last number should be greater than or equal to the first number.")

            # If input is valid, return the values
            if first_nr <= last_nr:
                return formula, first_nr, last_nr

        # Handle input errors and prompt user again
        except (ValueError, Exception) as ve:
            print(f"Error giving inputs: {ve}")
            pass


def calculating(formula, first_nr, last_nr):    # Function to perform calculations based on the provided formula and range
    # Evaluate the formula for each value of x and append the result to the list
    result_list = []
    for x in range(first_nr, last_nr + 1):
        try:
            result = eval(formula.replace('x', str(x)))
            result_list.append(result)
        
        # Handle formula evaluation errors and display an error message
        except (SyntaxError, ZeroDivisionError, NameError) as e:
            print(f"Error evaluating formula for x={x}: {e}")
    print(result_list)


if __name__ == '__main__':
    main()