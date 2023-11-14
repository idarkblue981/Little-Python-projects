def main():
    while True:
        a, b, c, d = inputs()
        result = calculator(a, b, c, d)
        print(f'The determinant is: {result}.')

def inputs():
    while True:
        try:
            a = int(input('Enter line 1, row 1: '))
            b = int(input('Enter line 1, row 2: '))
            c = int(input('Enter line 2, row 1: '))
            d = int(input('Enter line 2, row 2: '))
            return a, b, c, d
        except ValueError:
            pass

def calculator(a, b, c, d):
    term1 = a * c
    term2 = b * d
    result = term1 - term2
    return result

if __name__ == '__main__':
    main()
