def main():
    while True:
        try:
            unit = input("Enter the temperature unit (Celsius, Fahrenheit, Kelvin) or 'exit' to quit: ").strip().title()

            if unit.lower() == "exit":
                break

            if unit not in ["Celsius", "Fahrenheit", "Kelvin"]:
                print("Invalid unit! Please choose between Celsius, Fahrenheit, or Kelvin.")
                continue

            temp = float(input("Enter the temperature: "))

            # Conversions
            celsius_to_fahrenheit = 9/5 * temp + 32
            celsius_to_kelvin = temp + 273.15

            fahrenheit_to_celsius = (temp - 32) * (5 / 9)
            fahrenheit_to_kelvin = (temp - 32) * (5 / 9) + 273.15

            kelvin_to_celsius = temp - 273.15
            kelvin_to_fahrenheit = 1.8 * (temp - 273.15) + 32

            if unit == "Celsius":
                print(f"{temp} degrees Celsius = {celsius_to_fahrenheit:.2f} degrees Fahrenheit = {celsius_to_kelvin:.2f} degrees Kelvin.")
            elif unit == 'Fahrenheit':
                print(f"{temp} degrees Fahrenheit = {fahrenheit_to_celsius:.2f} degrees Celsius = {fahrenheit_to_kelvin:.2f} degrees Kelvin.")
            elif unit == 'Kelvin':
                print(f"{temp} degrees Kelvin = {kelvin_to_celsius:.2f} degrees Celsius = {kelvin_to_fahrenheit:.2f} degrees Fahrenheit.")
        except ValueError:
            print("Invalid temperature input! Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    main()
