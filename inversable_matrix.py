def main():
    while True:
        a, b, c, d = inputs()
        calculator(a, b, c, d)

def inputs():
    while True:
        try:
            a = float(input('Enter line 1, row 1: '))
            b = float(input('Enter line 1, row 2: '))
            c = float(input('Enter line 2, row 1: '))
            d = float(input('Enter line 2, row 2: '))
            return a, b, c, d
        except ValueError:
            pass

def calculator(a, b, c, d):
    det =  a * d - b * c

    if det == 0:
        print('This matrix is not invertible.')

    else:
        e = (1 / det) * abs(d)
        f = (1 / det) * -1 * abs(b)
        g = (1 / det) * -1 * abs(c)
        h = (1 / det) * abs(a)

        print(f'The inverse of the given metrix has the elements: {e}, {f}, {g} and {h}.')

if __name__ == '__main__':
    main()
