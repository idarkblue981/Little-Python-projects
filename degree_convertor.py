def main():
    temp()


def temp():
    while True:
        try:
            unit = input('Write which temperature measurement unit you want to use (between Celsius, Fahrenheit and Kelvin): ').strip().title()
            temp = float(input('Write the temperature: '))

    #Celsius

            C_F1 = 9/5 * temp
            C_F = C_F1 + 32

            C_K = temp + 273.15

    #Fahrenheit

            F_C1 = temp - 32
            F_C = F_C1 * 5/9

            F_K1 = temp - 32
            F_K = F_K1 * 5/9 + 273.15

    #Kelvin

            K_C = temp - 273.15

            K_F1 = temp - 273.15
            K_F = 1.8 * K_F1 + 32

            if unit == 'Celsius':
                print(temp, 'degrees Celsius =', C_F ,'degrees Fahrenheit =', C_K ,'degrees Kelvin.')
            elif unit == 'Fahrenheit':
                print(temp, 'degrees Fahrenheit =', F_K ,'degrees Kelvin =', F_C ,'degrees Celsius.')
            elif unit == 'Kelvin':
                print(temp, 'degrees Kelvin =', K_C ,'degrees Celsius =', K_F ,'degrees Fahrenheit.')
            else:
                print('Write another temperature measurement unit, between Celsius, Fahrenheit and Kelvin.')
                main()
        except ValueError:
            pass

main()
