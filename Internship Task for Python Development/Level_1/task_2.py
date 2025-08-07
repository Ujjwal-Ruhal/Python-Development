# Task 2: Temperature Conversion

# Assign the value
# copy ° symbol to chrome

CELSIUS = 1
FAHRENHEIT = 2

while True:
    print("\n****************************************")

    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    print("\n****************************************")

    choice = int(input("Enter your choice (1 or 2): "))

    # Celsius to Fehrenheit
    if choice == CELSIUS:
        value = float(input("Enter value in Celsius: "))
        fah = (value * 9/5) + 32
        print(f"The Fahrenheit is: {fah:.2f}°C \nThank You")

    # Fehrenheit to Celsius
    elif choice == FAHRENHEIT:
        value = float(input("Enter value in Fahrenheit: "))
        cel = (value - 32) * 5/9
        print(f"The Celsius is: {cel:.2f}°F \nThank You")

    # If user enters an invalid option
    else:
        print("Please choose a correct option (1 or 2)")
